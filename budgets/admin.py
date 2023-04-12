from django.contrib import admin
from .models import Budget


@admin.register(Budget)
class BudgetsAdmin(admin.ModelAdmin):
    list_display = (
        "budget_name",
        "amount",
        "start_date",
        "end_date"
    )
    