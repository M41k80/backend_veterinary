"""
URL configuration for apps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView



schema_view = get_schema_view(
    openapi.Info(
        title="Veterinary API",
        default_version='v1',
        description="Documentación de la API del sistema de la veterinaria",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vetclinicapiv1@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/', include('apps.appointments.urls')),
    path('api/', include('apps.services.urls')),
    path('api/', include('apps.dashboard.urls')),
    path('api/', include('apps.pets.urls')),
    path('api/', include('apps.users.urls')),
    path('api/', include('apps.schedules.urls')),
    path('api/', include('apps.communications.urls')),
    path('api/', include('apps.medicalRecord.urls')),
    path('api/', include('apps.store.urls')),
    path('api/', include('apps.reviews.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]


