from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from djmoney.forms.widgets import MoneyWidget
from .models import RepeatableTransaction, Transaction


class AddSingleTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        currency_choices = (
            ("PLN", "PLN"),
            ("USD", "USD"),
            ("EUR", "EUR"),
        )
        
        fields = (
            "description",
            "amount",
            "execution_date",
            "is_executed",
            "category",
            "type",
            "budget",
        )
        labels = {
            "type": _("Type"),
            "amount": _("Amount"),
            "category": _("Category"),
            "budget": _("Budget"),
            "execution_date": _("Execution date"),
            "is_executed": _("Is executed?"),
            "description": _("Description")
        }
        widgets = {
            "type": forms.widgets.Select(attrs={"required": True}),
            "amount": MoneyWidget(
                amount_widget=forms.widgets.NumberInput(
                    attrs={
                        "min":0,
                        "step":0.01,
                        "placeholder": _("Amount"),
                        "class": "form-control"},
                    
                ),
                currency_widget=forms.widgets.Select(
                    attrs={"class": "form-select"},
                    choices=currency_choices),
                default_currency = "PLN"
                ),
            "description": forms.widgets.Textarea(attrs={"rows": "3"})
        }
        
            
class AddRepeatableTransactionForm(forms.ModelForm):
    class Meta:
        model = RepeatableTransaction
        currency_choices = (
            ("PLN", "PLN"),
            ("USD", "USD"),
            ("EUR", "EUR"),
        )
        
        fields = (
            "description",
            "base_amout",
            "start_date",
            "end_date",
            "recurrence_type",
            "recurrence_value",
            "category",
            "type",
            "budget",
        )
        labels = {
            "type": _("Type"),
            "base_amout": _("Base Amount"),
            "category": _("Category"),
            "budget": _("Budget"),
            "start_date": _("From date"),
            "end_date": _("To date"),
            "recurrence_type": _("Period type"),
            "recurrence_value": _("Period lenght"),
            "description": _("Description")
        }
        widgets = {
            "type": forms.widgets.Select(attrs={"required": True}),
            "base_amout": MoneyWidget(
                amount_widget=forms.widgets.NumberInput(
                    attrs={
                        "min":0,
                        "step":0.01,
                        "placeholder": _("Amount"),
                        "class": "form-control"},
                    
                ),
                currency_widget=forms.widgets.Select(
                    attrs={"class": "form-select"},
                    choices=currency_choices),
                default_currency = "PLN"
                ),
            "recurrence_value": forms.widgets.NumberInput(
                    attrs={
                        "min":0,
                        "step":1,
                        "placeholder": _("Amount"),
                        "class": "form-control"},
                    
                ), 
            "description": forms.widgets.Textarea(attrs={"rows": "3"})
        }
        validators = {
            "recurrence_value": [
                MinValueValidator(1), 
                MaxValueValidator(366)
            ]
        }
        
    def clean_recurrence_value(self):
        max_values = {
            'DAILY': 1,
            'WEEKLY': 7,
            'MONTHLY': 31,
            'ANNUALLY': 366,
        }
        choice = self.cleaned_data.get('recurrence_type')
        max_value = max_values.get(choice)
        number = self.cleaned_data.get('recurrence_value')
        if number > max_value:
            raise forms.ValidationError(f'Maksymalna dozwolona wartość dla opcji {choice} to {max_value}.')
        return number
