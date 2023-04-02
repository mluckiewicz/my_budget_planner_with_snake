from django.urls import path
from . import views


app_name = "planner"


urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
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
    path(
        "edit_transaction_single/",
        views.edit_transaction_single,
        name="edit_transaction_single",
    ),
    path(
        "edit_transaction_repeatable/",
        views.edit_transaction_repeatable,
        name="edit_transaction_repeatable",
    ),
    path("search/", views.search, name="search"),
    path("calendar_view/", views.calendar_view, name="calendar_view"),
]
