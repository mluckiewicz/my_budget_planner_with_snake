from django.forms import ModelForm, Select
from django.utils.translation import gettext_lazy as _

from .models import Transaction


class SingleTransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = (
            'description',
            'amount',
            'execution_date',
            'is_executed',
            'category',
            'type',
            'budget'
        )
        labels = {
            'type': _('Typ'),
            'category': _('Kategoria'),
            'budget': _('Budżet'),
        }
        widgets = {
            'type': Select(attrs={'class': 'form-select'}),
            'category': Select(attrs={'class': 'form-select'}),
            'budget': Select(attrs={'class': 'form-select'}),
        }