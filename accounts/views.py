from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.html import format_html

from accounts.forms import CreateUserForm

from django.contrib.auth.decorators import login_required

def login_page(request):
    # return HttpResponse("login page")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'email or password incorrect - you can reset password below')
            return redirect('login')

    else:
        return render(request, 'login.html', {})


def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)
    # return HttpResponse("user register page")


def logout_page(request):
    logout(request)
    return redirect('login')
