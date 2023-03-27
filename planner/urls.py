from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('add_transaction_single/',views.register,name='add_transaction_single'),
    path('add_transaction_repeatable/', views.register, name='add_transaction_repeatable'),
    path('edit_transaction_single/', views.register, name='edit_transaction_single'),
    path('edit_transaction_repeatable/', views.register, name='edit_transaction_repeatable'),
    path('search/', views.register, name='search'),
    path('calendar_view/', views.register, name='calendar_view'),

]