from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.
from django.http import HttpResponse


def home(request):
    return redirect("login") # -> accounts.login


def dashboard(request):
    return render(request, "base.html")


def add_transaction_single(request):
    return HttpResponse("New single transaction")


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
