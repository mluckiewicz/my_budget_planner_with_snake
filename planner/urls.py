from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='planner/logout.html'), name='logout'),
    path('register/', views.register_page, name='register'),
    path('add_transaction_single/',views.add_transaction_single,name='add_transaction_single'),
    path('add_transaction_repeatable/', views.add_transaction_repeatable, name='add_transaction_repeatable'),
    path('edit_transaction_single/', views.edit_transaction_single, name='edit_transaction_single'),
    path('edit_transaction_repeatable/', views.edit_transaction_repeatable, name='edit_transaction_repeatable'),
    path('search/', views.search, name='search'),
    path('calendar_view/', views.calendar_view, name='calendar_view'),

]