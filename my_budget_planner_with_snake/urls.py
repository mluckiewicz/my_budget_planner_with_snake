from django.contrib import admin
from django.urls import path, include
from accounts.views import AuthRedirectView


urlpatterns = [
    path('', AuthRedirectView.as_view(pattern_name="login")),
    path('planner/', include('planner.urls')),
    path('account/', include('accounts.urls')),
    path('categories/', include('categories.urls')),
    path('budgets/', include('budgets.urls')),
    path('admin/', admin.site.urls),
]