from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import RepeatableTransaction, Transaction
import datetime


@receiver(post_save, sender=RepeatableTransaction)
def create_repeatable_transactions(sender, instance, created, **kwargs):
    """ 
    Catches a signal to add a new record to the Recurring Transactions table. Based 
    on the number of repetitions, adds the appropriate number of records to the 
    Transactions table.
    """
    if created:
        num_repeats = instance.recurrence_value
        for _ in range(num_repeats):
            # Calculate execution date
            
            
            
            # Add new record 
            transaction = Transaction.objects.create(
                description = instance.description,
                amount = instance.base_amout,
                execution_date = datetime.datetime.now().date(),
                user = instance.user,
                category = instance.category,
                type = instance.type,
                repeatable_transaction = instance,
                budget = instance.budget
            )
            transaction.save()
            
            
 # Signal registration           
post_save.connect(create_repeatable_transactions, sender=RepeatableTransaction)