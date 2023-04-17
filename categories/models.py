from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Type(models.Model):
    # Fields
    type_name = models.CharField(max_length=20, unique=True)

    # Meta class
    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    # Methods
    def __str__(self):
        return self.type_name


class Category(models.Model):
    # Fields
    category_name = models.CharField(max_length=255, null=False)
    default = models.BooleanField(default=False)
    users = models.ManyToManyField(User, through='UserCategory')
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    # Meta class
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    # Methods
    def __str__(self):
        return self.category_name
    

class UserCategory(models.Model):
    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    # Meta class
    class Meta:
        verbose_name = "User Category"
        verbose_name_plural = "User Categories"
        unique_together = ('user', 'category')