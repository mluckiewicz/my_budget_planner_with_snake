from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path(
        "login/",
        views.AuthLoginview.as_view(template_name="account/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="account/logout.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),
    path("register_done/", views.register_done, name="register_done"),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),



    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_done.html"
        ),
        name="password_reset_complete",
    ),
]
