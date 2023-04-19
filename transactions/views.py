from __future__ import annotations
import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import AddSingleTransactionForm, AddRepeatableTransactionForm
from .models import Transaction, RepeatableTransaction
from categories.models import Type, Category, UserCategory


class TransactionMixin:
    """A mixin for views that deal with transactions."""

    def get_context(self, request, form=None):
        """Generate a dictionary with data to pass to the template.

        Args:
            request: An HttpRequest object.
            form: An optional Form object.

        Returns:
            A dictionary with the form, back URL, and type-to-category mapping.
        """
        context = {}
        if form:
            context["form"] = form
        else:
            context["form"] = self.form_class()
        context["back_url"] = request.GET.get("back_url", "/transactions/")
        context["type_to_category"] = self.get_categories(request)
        return context

    def get_categories(self, request):
        """Retrieve available categories for each transaction type.

        Args:
            request: An HttpRequest object.

        Returns:
            A JSON-formatted string representing a dictionary mapping transaction types 
            to lists of available categories.
        """
        types = Type.objects.all()
        user_categories = UserCategory.objects.filter(user=request.user)
        categories = Category.objects.filter(
            id__in=user_categories.values_list("category_id", flat=True)
        )

        type_to_category = {}
        for t in types:
            category_list = [[c.id, c.category_name] for c in categories if c.type == t]
            type_to_category[t.id] = category_list

        return json.dumps(type_to_category)


@method_decorator(login_required, name="dispatch")
class AddSingleTransactionView(View, TransactionMixin):
    template_name = "transaction/add_transaction_single.html"
    form_class = AddSingleTransactionForm

    def get(self, request):
        return render(request, self.template_name, self.get_context(request))

    def post(self, request):
        # Check if the form is valid
        form = self.form_class(request.POST)
        if form.is_valid():
            # Add new transaction
            transaction = Transaction.objects.create(
                user=self.request.user,
                type=form.cleaned_data["type"],
                amount=form.cleaned_data["amount"],
                category=form.cleaned_data["category"],
                budget=form.cleaned_data["budget"],
                execution_date=form.cleaned_data["execution_date"],
                is_executed=form.cleaned_data["is_executed"],
                description=form.cleaned_data["description"],
            )
            transaction.save()

            # Redirect back to main form
            back_url = request.POST.get("back_url", None)
            if back_url is not None and back_url != "None":
                return redirect(back_url)
            return redirect(request.path)
        else:
            # Form is not valid, display errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

        return render(request, self.template_name, self.get_context(request, form))


@method_decorator(login_required, name="dispatch")
class AddRepeatableTransactionView(View, TransactionMixin):
    template_name = "transaction/add_transaction_repeatable.html"
    form_class = AddRepeatableTransactionForm

    def get(self, request):
        return render(request, self.template_name, self.get_context(request))

    def post(self, request):
        # Check if the form is valid
        form = self.form_class(request.POST)
        if form.is_valid():
            # Add new transaction
            transaction = RepeatableTransaction.objects.create(
                user=self.request.user,
                type=form.cleaned_data["type"],
                base_amout=form.cleaned_data["base_amout"],
                start_date=form.cleaned_data["start_date"],
                end_date=form.cleaned_data["end_date"],
                recurrence_type=form.cleaned_data["recurrence_type"],
                recurrence_value=form.cleaned_data["recurrence_value"],
                category=form.cleaned_data["category"],
                budget=form.cleaned_data["budget"],
                description=form.cleaned_data["description"],
            )
            transaction.save()

            # Redirect back to main form
            back_url = request.POST.get("back_url", None)

            if back_url is not None and back_url != "None":
                return redirect(back_url)
            return redirect(request.path)

        return render(request, self.template_name, self.get_context(request, form=form))


@method_decorator(login_required, name="dispatch")
class TransactionTableView(View):
    template_name = "transaction/table.html"

    def get(self, request):
        context = {}
        context["single_transactions"] = Transaction.objects.filter(user=request.user)
        context["repeatable_transactions"] = RepeatableTransaction.objects.filter(
            user=request.user
        )
        return render(request, self.template_name, context)


@method_decorator(login_required, name="dispatch")
class TransactionUpdateView(UpdateView, TransactionMixin):
    model = Transaction
    form_class = AddSingleTransactionForm
    template_name = "transaction/edit_single.html"
    success_url = reverse_lazy("transactions:transactions")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["back_url"] = self.request.GET.get("back_url", "/transactions/")
        context["type_to_category"] = self.get_categories(self.request)
        return context


def delete_transactions(request) -> JsonResponse[dict]:
    """
    Deletes the selected categories from the database. Uses AJAX equest form template
    """
    if request.method == "POST":
        ids = request.POST.getlist("ids[]")
        if request.POST.getlist("table")[0] == "table_single":
            Transaction.objects.filter(id__in=ids).delete()
        else:
            RepeatableTransaction.objects.filter(id__in=ids).delete()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False, "message": "Invalid request method"})
