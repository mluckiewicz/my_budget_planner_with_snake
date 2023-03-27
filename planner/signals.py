from __future__ import annotations
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import RepeatableTransaction, Transaction
from .utils.date_generator import DateCalculator


@receiver(post_save, sender=RepeatableTransaction)
def create_repeatable_transactions(sender, instance, created, **kwargs):
    """ 
    Catches a signal to add a new record to the Recurring Transactions table. Based 
    on the number of repetitions, adds the appropriate number of records to the 
    Transactions table.
    """

    if created:
        # Calculate execution date
        dc = DateCalculator(instance.start_date, instance.end_date)
        dates = dc.get_dates(instance.recurrence_type, instance.recurrence_value)
        
        for idx, value in enumerate(dates):
            # Add new record 
            transaction = Transaction.objects.create(
                description = instance.description,
                amount = instance.base_amout,
                execution_date = value,
                user = instance.user,
                category = instance.category,
                type = instance.type,
                repeatable_transaction = instance,
                budget = instance.budget
            )
            transaction.save()
            
            
 # Signal registration           
post_save.connect(create_repeatable_transactions, sender=RepeatableTransaction)