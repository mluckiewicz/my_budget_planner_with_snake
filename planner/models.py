from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Type(models.Model):
    # Fields
    type_name = models.CharField(max_length=20, unique=True)

    # Methods
    def __str__(self):
        return self.type_name


class Category(models.Model):
    # Fields
    category_name = models.CharField(max_length=255, null=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    # Methods
    def __str__(self):
        return self.category_name


class Budget(models.Model):
    # Fields
    budget_name = models.CharField(max_length=255, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    start_date = models.DateField(default=timezone.now, null=False)
    end_date = models.DateField(default=timezone.now, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Methods
    def __str__(self):
        return self.budget_name


class RepeatableTransaction(models.Model):
    # Choises for recurrence_type field
    class RecurrenceTypes(models.TextChoices):
        DAILY = "DAILY", _("Daily")
        WEEKLY = "WEEKLY", _("Weekly")
        MONTHLY = "MONTHLY", _("Monthly")
        QUATERLY = "QUATERLY", _("Quaterly")
        ANNUALLY = "ANNUALLY", _("Annually")

    # Fields
    description = models.CharField(max_length=255)
    base_amout = models.DecimalField(max_digits=10, decimal_places=2, null=False)
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=None)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, default=None)

    # Methods
    def __str__(self):
        return self.description


class Transaction(models.Model):
    # Fields
    description = models.CharField(max_length=255, blank=False, null=False)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, null=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    execution_date = models.DateField(auto_now=True)
    is_executed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=None)
    repeatable_transaction = models.ForeignKey(
        RepeatableTransaction, null=True, on_delete=models.CASCADE
    )
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    # Methods
    def __str__(self):
        return self.description
