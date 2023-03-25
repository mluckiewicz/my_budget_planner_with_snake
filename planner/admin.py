from django.contrib import admin
from .models import Categories, Transactions, Types, Frequencies, RepeatableTransactions


@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display = ("type_name",)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        "category_name",
        "type",
    )


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "category",
        "description",
        "amount",
        "transaction_type",
        "is_repatable",
        "created",
        "updated",
    )


@admin.register(Frequencies)
class FrequenciesAdmin(admin.ModelAdmin):
    list_display = (
        "frequency_name",
    )
    
    
@admin.register(RepeatableTransactions)
class RepeatableTransactionsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "start_date",
        "end_date",
        "transaction_type",
        "category",
        "frequency",
        
    )