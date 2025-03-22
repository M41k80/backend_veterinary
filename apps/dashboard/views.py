from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from apps.appointments.models import Appointment

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_dashboard(request):
    if resquest.user != 'admin':
        return Response({'error': 'You are not authorized to access this page'}, status=403)
    
    total_appointments = Appointment.objects.all().count()
    completed_appointments = Appointment.objects.filter(status='completed').count()
    total_earnings = Appointment.objects.filter(status='completed').aggregate(Sum('total_cost'))['total_cost__sum'] or 0
    
    data = {
        'total_appointments': total_appointments,
        'completed_appointments': completed_appointments,
        'total_earnings': total_earnings,
    }

    return Response(data)