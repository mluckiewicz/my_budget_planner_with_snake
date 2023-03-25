from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Types(models.Model):
    
    # Fields
    type_name = models.CharField(max_length=20, unique=True)
    
    # Methods
    def __str__(self):
        return self.type_name

    
class Categories(models.Model):
    
    # Fields
    category_name = models.CharField(max_length=255, blank=False)
    type = models.ForeignKey(Types, on_delete=models.CASCADE)
    
    # Methods
    def __str__(self):
        return self.category_name




class Frequencies(models.Model):
    
    # Fields
    frequency_name = models.CharField(max_length=255)
    
    # Methods
    def __str__(self):
        return self.frequency_name


class RepeatableTransactions(models.Model):
    
    # fields
    description = models.CharField(max_length=255)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    num_occurrences = models.IntegerField(default=1)
    frequency_days = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    frequency = models.ForeignKey(Frequencies, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(Types, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    # Methods
    def __str__(self):
        return self.description
    
    
class Transactions(models.Model):

    # Fields
    description = models.CharField(max_length=255, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    is_repatable = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(Types, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    repeatable_transaction = models.ForeignKey(RepeatableTransactions, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    execution_date = models.DateField(auto_now=True)
    is_executed = models.BooleanField(default=False)
    
    # Methods
    def __str__(self):
        return self.description

    