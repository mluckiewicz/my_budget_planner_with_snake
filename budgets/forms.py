from django import forms
from django.utils.translation import gettext_lazy as _
from djmoney.forms.widgets import MoneyWidget
from .models import Budget

        
class AddBudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        currency_choices = (
            ("PLN", "PLN"),
            ("USD", "USD"),
            ("EUR", "EUR"),
        )
        
        fields = (
            "budget_name",
            "amount",
            "start_date",
            "end_date",
        )
        labels = {
            "budget_name": _("Naazwa budżetu"),
            "amount": _("Kwota"),
            "start_date": _("Od kiedy obowiązuje"),
            "end_date": _("Do kiedy obowiązuje"),
        }
        widgets = {
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
        }
        