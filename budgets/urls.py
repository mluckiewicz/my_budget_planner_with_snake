from django.urls import path
from . import views


app_name = "budgets"


urlpatterns = [
    path("", 
         views.BudgetTableView.as_view(), 
         name="budgets"
    ),
    path(
        "add_budget/",
        views.AddBudgetView.as_view(),
        name="add_budget",
    ),
    path(
        "delete_budget/",
        views.delete_budget,
        name="delete_budget",
    ),
    path(
        "edit/<int:pk>/",
        views.BudgetUpdateView.as_view(),
        name="edit_budget",
    ),
]
