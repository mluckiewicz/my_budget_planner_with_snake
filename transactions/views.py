from __future__ import annotations
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import (
    AddSingleTransactionForm,
    AddRepeatableTransactionForm
)
from .models import Transaction, RepeatableTransaction


@method_decorator(login_required, name="dispatch")
class AddSingleTransactionView(FormView):
    form_class = AddSingleTransactionForm
    template_name = "transaction/add_transaction_single.html"
    success_url = "/dashboard/"

    def form_valid(self, form):
        current_user = self.request.user

        Transaction.objects.create(
            user=current_user,
            type=form.cleaned_data["type"],
            amount=form.cleaned_data["amount"],
            category=form.cleaned_data["category"],
            budget=form.cleaned_data["budget"],
            execution_date=form.cleaned_data["execution_date"],
            is_executed=form.cleaned_data["is_executed"],
            description=form.cleaned_data["description"],
        )
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class AddRepeatableTransactionView(FormView):
    form_class = AddRepeatableTransactionForm
    template_name = "transaction/add_transaction_repeatable.html"
    success_url = "/dashboard/"

    def form_valid(self, form):
        current_user = self.request.user

        RepeatableTransaction.objects.create(
            user=current_user,
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
        return super().form_valid(form)
    
    
@method_decorator(login_required, name="dispatch")
class TransactionTableView(View):
    model = Transaction
    template_name = "transaction/table.html"
    context_object_name = "transactions"

    def get(self, request):
        context = {}
        transactions = self.model.objects.all()
        # Union of default categories with user added 
        context["transactions"] = transactions
        return render(request, self.template_name, context)
