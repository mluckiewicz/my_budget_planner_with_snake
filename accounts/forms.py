from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']