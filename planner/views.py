from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import AddSingleTransactionForm, AddRepeatableTransactionForm
from .models import Transaction, RepeatableTransaction


# Create your views here.
from django.http import HttpResponse


def home(request):
    return redirect("login")  # -> accounts.login


def dashboard(request):
    return render(request, "base.html")


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


def add_transaction_repeatable(request):
    return HttpResponse("New repeatable transaction")


def edit_transaction_single(request):
    return HttpResponse("Edit single transaction")


def edit_transaction_repeatable(request):
    return HttpResponse("Edit single transaction")


def search(request):
    return HttpResponse("search view - full table with data chooser")


def calendar_view(request):
    return HttpResponse("view transaction on calendar")
