from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator


class RepeatableTransaction(models.Model):
    # Choises for recurrence_type field
    class RecurrenceTypes(models.TextChoices):
        DAILY = "DAILY", _("Daily")
        WEEKLY = "WEEKLY", _("Weekly")
        MONTHLY = "MONTHLY", _("Monthly")
        ANNUALLY = "ANNUALLY", _("Annually")

    # Fields
    description = models.CharField(max_length=255, blank=True)
    base_amout = MoneyField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default_currency="PLN",
        validators=[MinMoneyValidator(0)],
    )
    start_date = models.DateField(default=timezone.now, null=False)
    end_date = models.DateField(default=timezone.now, null=False)
    recurrence_type = models.CharField(
        max_length=10,
        choices=RecurrenceTypes.choices,
        default=RecurrenceTypes.DAILY,
        null=False,
    )
    recurrence_value = models.IntegerField(default=1, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        default=None,
        null=False,
    )
    type = models.ForeignKey(
        "categories.Type",
        on_delete=models.CASCADE,
        default=None,
    )
    budget = models.ForeignKey('budgets.Budget', on_delete=models.CASCADE, default=None)

    # Meta class
    class Meta:
        verbose_name = "RepeatableTransaction"
        verbose_name_plural = "RepeatableTransactions"

    # Methods
    def __str__(self):
        return self.description


class Transaction(models.Model):
    # Fields
    description = models.CharField(max_length=255, blank=True)
    amount = MoneyField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
        default_currency="PLN",
        validators=[MinMoneyValidator(0)],
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    execution_date = models.DateField(default=timezone.now)
    is_executed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        default=None,
    )
    type = models.ForeignKey(
        "categories.Type",
        on_delete=models.CASCADE,
        default=None,
    )
    repeatable_transaction = models.ForeignKey(
        RepeatableTransaction, blank=True, null=True, on_delete=models.CASCADE
    )
    budget = models.ForeignKey('budgets.Budget', on_delete=models.CASCADE)

    # Meta class
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    # Methods
    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('transactions:transaction_detail', args=(self.id,))
