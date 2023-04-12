from __future__ import annotations
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .forms import AddBudgetForm
from .models import Budget


# Create your views here.
@method_decorator(login_required, name="dispatch")
class BudgetTableView(View):
    model = Budget
    template_name = "budget/table.html"
    context_object_name = "budgets"

    def get(self, request):
        context = {}
        user_added = Budget.objects.filter(user=request.user)
        # Union of default categories with user added 
        context["budgets"] = user_added
        return render(request, self.template_name, context)

    
@method_decorator(login_required, name="dispatch")
class AddBudgetView(View):
    template_name = "budget/add.html"
    form_class = AddBudgetForm

    def get(self, request):
        return render(request, self.template_name, self.get_context(request))

    def post(self, request):
        # Check if the form is valid
        form = self.form_class(request.POST)
        if form.is_valid():
            # Add new category
            budget = Budget.objects.create(
                budget_name=form.cleaned_data["budget_name"],
                amount=form.cleaned_data["amount"],
                start_date=form.cleaned_data["start_date"],
                end_date=form.cleaned_data["end_date"],
                user=request.user,
            )
            budget.save()

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
class BudgetUpdateView(UpdateView):
    model = Budget
    form_class = AddBudgetForm
    template_name = 'budget/edit.html'
    success_url = reverse_lazy('budgets:budgets')
        
    
def delete_budget(request) -> JsonResponse[dict]:
    """
    Deletes the selected categories from the database. Uses AJAX equest form template

    Args:
        request: The HTTP request object.

    Returns:
        A JSON response containing a success flag and, if applicable, an error message.

    Raises:
        N/A
    """
    if request.method == 'POST':
        ids = request.POST.getlist('ids[]')
        Budget.objects.filter(id__in=ids).delete()    
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})