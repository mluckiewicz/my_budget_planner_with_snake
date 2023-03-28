from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from django.http import HttpResponse
from .forms import CreateUserForm


def login(request):
    # return HttpResponse("login page")
    return render(request, 'planner/login.html')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'planner/register.html', context)
    # return HttpResponse("user register page")


def index(request):
    return HttpResponse("main page - DASHBOARD")


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