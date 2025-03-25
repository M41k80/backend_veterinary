from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from apps.store.models import Product, Order, Cart

class AdminDashboard(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'category']
    search_fields = ['name', 'category']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        return queryset

admin.site.register(Product, AdminDashboard)
admin.site.register(Order)
admin.site.register(Cart)