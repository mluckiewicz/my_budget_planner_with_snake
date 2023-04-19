from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm, UpdateUserForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return render(request, "account/register_done.html", {"new_user": new_user})
    else:
        form = UserRegistrationForm()
    return render(request, "account/register.html", {"form": form})


def register_done(request):
    context = {}
    return render(request, 'account/register_done.html', context)


@login_required
def user_profile(request):
    context = {}
    return render(request, 'account/user_profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()

            return render(request, 'account/user_profile.html', {})

    else:
        user_form = UpdateUserForm(instance=request.user)
    context = {'user_form': user_form}
    return render(request, 'account/edit_profile.html', context)


class AuthRedirectView(RedirectView):
    """
    Redirects authenticated users to the dashboard, otherwise to the login page.

    If the user is authenticated, this view will redirect to the dashboard page
    using the URL defined by the 'planner:dashboard' named URL pattern.
    If the user is not authenticated, this view will call the 'get_redirect_url'
    method of the parent class to get the redirect URL. By default, this will
    redirect to the URL defined by the 'login' named URL pattern.
    """

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('dashboard:dashboard')
        else:
            return super().get_redirect_url(*args, **kwargs)
        
        
class AuthLoginview(LoginView):
    """
    Displays the login page and logs the user in if valid credentials are submitted.

    This view is based on Django's built-in 'LoginView' class and inherits all of
    its functionality, including form validation, authentication, and redirecting.
    By default, this view will use the 'account/login.html' template and will
    redirect authenticated users to the dashboard URL defined by the 'planner:dashboard'
    named URL pattern. This behavior can be customized by setting the 'template_name',
    'redirect_authenticated_user', and 'success_url' attributes.

    Attributes:
        template_name (str): The name of the template to use for the login page.
            Defaults to 'account/login.html'.
        redirect_authenticated_user (bool): Whether to redirect authenticated
            users to the success URL instead of the login page. Defaults to True.
        success_url (str): The URL to redirect to after successful login.
            Defaults to the URL defined by the 'planner:dashboard' named URL pattern.
    """
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard:dashboard')
    
