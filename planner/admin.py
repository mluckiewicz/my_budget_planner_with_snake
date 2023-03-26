from django.contrib import admin
from .models import (
    Types,
    Categories,
    Budgets,
    RepeatableTransactions,
    Transactions
)

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display = ("type_name",)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        "category_name",
        "type",
    )


@admin.register(Budgets)
class BudgetsAdmin(admin.ModelAdmin):
    list_display = (
        "budget_name",
        "amount",
        "start_date",
        "end_date"
    )
    
    
@admin.register(RepeatableTransactions)
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


@admin.register(Transactions)
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

