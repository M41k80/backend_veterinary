from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from apps.appointments.models import Appointment
from apps.store.models import Product, Order, OrderItem

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_dashboard(request):
    
    total_appointments = Appointment.objects.all().count()
    completed_appointments = Appointment.objects.filter(status='completed').count()
    total_earnings = Appointment.objects.filter(status='completed').aggregate(Sum('total_cost'))['total_cost__sum'] or 0
    
    data = {
        'total_appointments': total_appointments,
        'completed_appointments': completed_appointments,
        'total_earnings': total_earnings,
    }

    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_dashboard_data(request):
    # Store Sales Data
    total_revenue = OrderItem.objects.filter(order__status='paid').aggregate(total=Sum('price'))['total'] or 0
    total_completed_orders = Order.objects.filter(status='completed').count()

    # MOST SELLING PRODUCTS
    top_products = OrderItem.objects.values('product__name')\
        .annotate(total_quantity=Sum('quantity'))\
        .order_by('-total_quantity')[:5]

    # TOTAL PRODUCTS IN STOCK
    total_products_in_stock = Product.objects.aggregate(total_stock=Sum('stock'))['total_stock'] or 0

    # Store Data
    data = {
        'store': {
            'total_revenue': total_revenue,
            'total_completed_orders': total_completed_orders,
            'top_products': top_products,
            'total_products_in_stock': total_products_in_stock,
        },
    }
    
    return Response(data)