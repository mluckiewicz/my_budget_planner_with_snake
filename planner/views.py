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


def add_transaction_repeatable(request):
    return HttpResponse("New repeatable transaction")

def edit_transaction_single(request):
    return HttpResponse("Edit single transaction")


def add_transaction_repeatable(request):
    return HttpResponse("Edit repeatable transaction")


def search(request):
    return HttpResponse("search view - full table with data chooser")

def calendar_view(request):
    return HttpResponse("view transaction on calendar")