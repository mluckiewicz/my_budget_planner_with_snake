from django.contrib import admin
from django.urls import path, include
from accounts.views import AuthRedirectView


urlpatterns = [
    path('', AuthRedirectView.as_view(pattern_name="login")),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('categories/', include('categories.urls')),
    path('budgets/', include('budgets.urls')),
    path('transactions/', include('transactions.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]