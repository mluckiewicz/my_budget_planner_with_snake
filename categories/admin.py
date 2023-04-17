from django.contrib import admin
from .models import (
    Type,
    Category,
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