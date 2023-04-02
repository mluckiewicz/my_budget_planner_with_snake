from django import forms
from django.utils.translation import gettext_lazy as _
from djmoney.forms.fields import MoneyField
from .models import Transaction, Type, Category, Budget


class SingleTransactionForm(forms.Form):
    currency_choices = (
        ("PLN", "PLN"),
        ("USD", "USD"),
        ("EUR", "EUR"),
    )

    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        required=True,
        label=_("Typ"),
    )
    amount = MoneyField(
        currency_widget=forms.widgets.Select(
            attrs={"class": "form-select"},
            choices=currency_choices,
        ),
        min_value=0,
        max_digits=10,
        decimal_places=2,
        default_amount=0,
        default_currency="PLN",
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        label=_("Kategoria"),
    )
    budget = forms.ModelChoiceField(
        queryset=Budget.objects.all(),
        required=True,
        label=_("Budżet"),
    )
    execution_date = forms.DateField(
        required=True,
        label=_("Data realizacji"),
    )
    is_executed = forms.BooleanField(
        required=False,
        label=_("Zrealizowa?"),
    )
    description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={"rows": "3"})
    )
