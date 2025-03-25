from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScheduleViewSet
from apps.appointments.views import AppointmentViewSet

router = DefaultRouter()
router.register(r'schedules', ScheduleViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]