from django.shortcuts import render, redirect
from .forms import SingleTransactionForm

from django.contrib import messages

# Create your views here.
from django.http import HttpResponse


def home(request):
    return redirect("login") # -> accounts.login


def dashboard(request):
    return render(request, "base.html")


def add_transaction_single(request):
    if request.method == "POST":
        form = SingleTransactionForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = SingleTransactionForm()
    return render(
        request,
        "transaction/add_transaction_single.html",
        context={"form": form},
    )


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
