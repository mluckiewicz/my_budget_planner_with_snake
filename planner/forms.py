from django import forms
from django.utils.translation import gettext_lazy as _
from djmoney.forms.fields import MoneyField
from djmoney.forms.widgets import MoneyWidget
from .models import Type, Category, Budget, RepeatableTransaction


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
        label=_("Kwota"),
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
        required=False, widget=forms.Textarea(attrs={"rows": "3"}),
        label=_("Notatka"),
    )


class RepeatableTransactionForm(forms.ModelForm):
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
            "recurrence_type": _("Rodzaj powtórzenia"),
            "recurrence_value": _("Okres powtórzenia"),
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