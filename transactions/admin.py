from django.contrib import admin
from .models import (
    RepeatableTransaction,
    Transaction,
)

    
@admin.register(RepeatableTransaction)
class RepeatableTransactionsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "start_date",
        "end_date",
        "base_amout",
        "recurrence_type",
        "recurrence_value",
        "category",
        "type",
        "budget"
    )
    list_filter = ('type', 'category', 'budget','user')
    search_fields = ['user__username', 'category__category_name', 'description']
    raw_id_fields = ('user',)
    date_hierarchy = 'start_date'
    ordering = ('category', 'start_date')


@admin.register(Transaction)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "type",
        "category",
        "description",
        "amount",
        "budget",
        "execution_date",
        "is_executed",
        "created",
        "updated",
    )
    list_filter = ('user', 'type', 'category', 'budget')
    search_fields = ['user__username', 'category__category_name', 'description']
    date_hierarchy = 'execution_date'
    ordering = ('category', 'execution_date')