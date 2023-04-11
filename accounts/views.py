from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from accounts.forms import CreateUserForm, UpdateUserForm



def login_page(request):
    # return HttpResponse("login page")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
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



def logout_page(request):
    logout(request)
    return redirect('login')


def user_profile(request):
    context = {}
    return render(request, 'user_profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('dashboard')
    else:
        user_form = UpdateUserForm(instance=request.user)
    context = {'user_form': user_form}
    return render(request, 'edit_profile.html', context)


