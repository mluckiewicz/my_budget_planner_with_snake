from django.urls import path
from . import views


app_name = "transactions"


urlpatterns = [
    path("", 
         views.TransactionTableView.as_view(), 
         name="transactions"
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
]
