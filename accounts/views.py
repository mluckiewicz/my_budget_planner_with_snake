from django.shortcuts import render, redirect
from .forms import CreateUserForm


def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "register.html", context)
