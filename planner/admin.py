from django.contrib import admin
from .models import (
    Type,
    Category,
    Budget,
    RepeatableTransaction,
    Transaction,
    UserCategory,
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


@admin.register(UserCategory)
class UserCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "category",
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