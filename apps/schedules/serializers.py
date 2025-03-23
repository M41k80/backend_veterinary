from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'veterinarian', 'start_time', 'end_time', 'is_available']
        
    def validate(self, data):
        start_time = data.get('start_time')
        schedule = data.get('schedule')
    
        if start_time and schedule:
            if start_time < schedule.start_time or start_time >= schedule.end_time:
                raise serializers.ValidationError("Start time must be between the start and end times of the schedule.")
    
        return data