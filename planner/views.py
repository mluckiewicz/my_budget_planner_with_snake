from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import SingleTransactionForm
from .models import Transaction


# Create your views here.
from django.http import HttpResponse


def home(request):
    return redirect("login")  # -> accounts.login


def dashboard(request):
    return render(request, "base.html")


class AddSingleTransactionView(FormView):
    form_class = SingleTransactionForm
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
