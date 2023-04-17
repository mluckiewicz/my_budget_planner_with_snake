from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator


class Budget(models.Model):
    # Fields
    budget_name = models.CharField(max_length=255, null=False)
    amount = MoneyField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default_currency="PLN",
        validators=[MinMoneyValidator(0)],
    )
    start_date = models.DateField(default=timezone.now, null=False)
    end_date = models.DateField(default=timezone.now, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Meta class
    class Meta:
        verbose_name = "Budget"
        verbose_name_plural = "Budgets"

    # Methods
    def __str__(self):
        return self.budget_name
