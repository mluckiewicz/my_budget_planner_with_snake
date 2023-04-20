from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords are not the same')
        # return cd['password2']


class UpdateUserForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("There is no this email address connected with any User! Please input correct email adress.")
        return email
