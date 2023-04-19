from __future__ import annotations
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .forms import AddCategoryForm
from .models import Category, UserCategory


@method_decorator(login_required, name="dispatch")
class CategoryTableView(View):
    model = Category
    template_name = "category/table.html"
    context_object_name = "categories"

    def get(self, request):
        context = {}
        categoires_default = Category.objects.filter(default=True)
        categories_users = Category.objects.filter(users=request.user)
        # Union of default categories with user added
        context["categories"] = categoires_default | categories_users
        return render(request, self.template_name, context)


@method_decorator(login_required, name="dispatch")
class AddCategoryView(View):
    template_name = "category/add.html"
    form_class = AddCategoryForm

    def get(self, request):
        return render(request, self.template_name, self.get_context(request))

    def post(self, request):
        # Check if the form is valid
        form = self.form_class(request.POST)
        if form.is_valid():
            # Add new category
            category = Category.objects.create(
                category_name=form.cleaned_data["category_name"],
                type=form.cleaned_data["type"],
            )
            category.save()

            # Assign category to user
            user_category = UserCategory(user=request.user, category=category)
            user_category.save()

            # Redirect back to main form
            back_url = request.POST.get("back_url", None)
            if back_url is not None and back_url != "None":
                return redirect(back_url)
            return redirect(request.path)

        return render(request, self.template_name, self.get_context(request))

    def get_context(self, request, form=None):
        # Helper method to generate a dictionary with data to pass to the template
        context = {}
        if form:
            context["form"] = form
        else:
            context["form"] = self.form_class()
        context["back_url"] = request.GET.get("back_url", None)
        return context


@method_decorator(login_required, name="dispatch")
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = AddCategoryForm
    template_name = "category/edit.html"
    success_url = reverse_lazy("categories:categories")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = kwargs.get("form", None)
        context["form"] = form if form else self.form_class()
        context["back_url"] = self.request.GET.get("back_url", "/categories/")
        return context


def delete_categories(request) -> JsonResponse[dict]:
    """
    Deletes the selected categories from the database. Uses AJAX equest form template

    Args:
        request: The HTTP request object.

    Returns:
        A JSON response containing a success flag and, if applicable, an error message.

    Raises:
        N/A
    """
    if request.method == "POST":
        ids = request.POST.getlist("ids[]")
        Category.objects.filter(id__in=ids).exclude(default=True).delete()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False, "message": "Invalid request method"})
