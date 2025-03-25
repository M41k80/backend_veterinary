from django.urls import path
from .views import admin_dashboard, get_dashboard_data

urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/store/', get_dashboard_data, name='dashboard_data'),
    
]

