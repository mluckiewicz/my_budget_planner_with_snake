from django.urls import path
from . import views


app_name = "planner"


urlpatterns = [
    path("dashboard/", 
         views.dashboard, 
         name="dashboard"
    ),
    path(
        "add_single/",
        views.AddSingleTransactionView.as_view(),
        name="add_single",
    ),
    path(
        "add_repeatable/",
        views.AddRepeatableTransactionView.as_view(),
        name="add_repeatable",
    ),
    path("budget/", 
         views.BudgetTableView.as_view(), 
         name="budget"
    ),
    path(
        "budget/add_budget/",
        views.AddBudgetView.as_view(),
        name="add_budget",
    ),
    path(
        "budget/delete_budget/",
        views.delete_budget,
        name="delete_budget",
    ),
    path(
        "budget/edit/<int:pk>/",
        views.BudgetUpdateView.as_view(),
        name="edit_budget",
    ),
    path("categories/", 
         views.CategoryTableView.as_view(), 
         name="categories"
    ),
    path(
        "categories/add_category/",
        views.AddCategoryView.as_view(),
        name="add_category",
    ),
    path(
        "categories/delete_categories/",
        views.delete_categories,
        name="delete_categories",
    ),
    path(
        "categories/edit/<int:pk>/",
        views.CategoryUpdateView.as_view(),
        name="edit_category",
    ),
    path("search/", views.search, name="search"),
    path("calendar_view/", views.calendar_view, name="calendar_view"),
]
