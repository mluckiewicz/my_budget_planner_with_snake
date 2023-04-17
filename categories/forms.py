from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Category

        
        
class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            "category_name",
            "type",
        )
        widgets = {
            "type": forms.widgets.Select(attrs={"required": True}),
        }
        