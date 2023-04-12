from django.urls import path
from . import views


app_name = "categories"


urlpatterns = [
    path("", 
         views.CategoryTableView.as_view(), 
         name="categories"
    ),
    path(
        "add_category/",
        views.AddCategoryView.as_view(),
        name="add_category",
    ),
    path(
        "delete_categories/",
        views.delete_categories,
        name="delete_categories",
    ),
    path(
        "edit/<int:pk>/",
        views.CategoryUpdateView.as_view(),
        name="edit_category",
    ),
]
