from django.urls import path
from . import views


app_name = "dashboard"


urlpatterns = [

    path(
        "",
        views.DashboardView.as_view(),
        name="dashboard",
    ),
    path('calendar_data/', views.calendar_data, name='calendar_data'),
    path('get_pending_list/', views.get_pending_list, name='get_pending_list')

]
