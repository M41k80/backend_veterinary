from rest_framework import serializers
from apps.appointments.models import Appointment
from apps.services.models import Service
from apps.services.serializers import ServiceSerializer
from apps.schedules.models import Schedule
from apps.schedules.serializers import ScheduleSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    service_ids = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True, write_only=True,
                                                     source='services')
    schedule = ScheduleSerializer(read_only=True)
    schedule_id = serializers.PrimaryKeyRelatedField(queryset=Schedule.objects.all(), write_only=True,
                                                     source='schedule')
    
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only = ['total_cost', 'end_time']
        
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        if 'services' in validated_data:
            instance.services.set(validated_data.get('services', instance.services.all()))
            instance.calculate_total_cost()
        if 'schedule' in validated_data:
            instance.schedule = validated_data.get('schedule', instance.schedule)
        instance.save()
        return instance