from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("home - login page")


def index(request):
    return HttpResponse("main page - DASHBOARD")


def register(request):
    return HttpResponse("user register page")


def add_transaction_single(request):
    return HttpResponse("New single transaction")

# def reset_password(request):
#     return HttpResponse("user register page")