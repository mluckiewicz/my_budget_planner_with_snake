from django.contrib import admin
from .models import (
    Type,
    Category,
    Budget,
    RepeatableTransaction,
    Transaction
)

@admin.register(Type)
class TypesAdmin(admin.ModelAdmin):
    list_display = ("type_name",)


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        "category_name",
        "type",
    )


@admin.register(Budget)
class BudgetsAdmin(admin.ModelAdmin):
    list_display = (
        "budget_name",
        "amount",
        "start_date",
        "end_date"
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


@admin.register(Transaction)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "type",
        "category",
        "description",
        "amount",
        "budget",
        "created",
        "updated",
    )

