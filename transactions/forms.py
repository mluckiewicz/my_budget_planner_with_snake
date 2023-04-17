from django import forms
from django.utils.translation import gettext_lazy as _
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
            "type": _("Typ"),
            "amount": _("Kwota"),
            "category": _("Kategoria"),
            "budget": _("Budżet"),
            "execution_date": _("Data realizacji"),
            "is_executed": _("Zrealizowana?"),
            "description": _("Opis")
        }
        widgets = {
            "type": forms.widgets.Select(attrs={"required": True}),
            "amount": MoneyWidget(
                amount_widget=forms.widgets.NumberInput(
                    attrs={
                        "min":0,
                        "step":0.01,
                        "placeholder": _("Wprowadź kwotę"),
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
            "type": _("Typ"),
            "base_amout": _("Kwota"),
            "category": _("Kategoria"),
            "budget": _("Budżet"),
            "start_date": _("Od kiedy"),
            "end_date": _("Do kiedy"),
            "recurrence_type": _("Rodzaj cyklu"),
            "recurrence_value": _("Długość cyklu"),
            "description": _("Opis")
        }
        widgets = {
            "type": forms.widgets.Select(attrs={"required": True}),
            "base_amout": MoneyWidget(
                amount_widget=forms.widgets.NumberInput(
                    attrs={
                        "min":0,
                        "step":0.01,
                        "placeholder": _("Wprowadź kwotę"),
                        "class": "form-control"},
                    
                ),
                currency_widget=forms.widgets.Select(
                    attrs={"class": "form-select"},
                    choices=currency_choices),
                default_currency = "PLN"
                ),

            "description": forms.widgets.Textarea(attrs={"rows": "3"})
        }
