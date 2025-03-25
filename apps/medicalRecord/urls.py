from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicalRecordView

router = DefaultRouter()
router.register(r'medical_records', MedicalRecordView, basename='medical_record')

urlpatterns = [
    path('', include(router.urls)),
]