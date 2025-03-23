from django.db import models
from apps.users.models import User

class Schedule(models.Model):
    veterinarian = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules', limit_choices_to={'role': 'veterinarian'})
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.veterinarian.username} - {self.start_time} - {self.end_time}"
    
    def generate_time_slots(self):
        time_slots = []
        current_time = self.start_time
        
        while current_time + timedelta(minutes=30) <= self.end_time:
            time_slots.append(current_time)
            current_time += timedelta(minutes=30)
        
        return time_slots

    def save(self, *args, **kwargs):
        overlapping_schedules = Schedule.objects.filter(
            veterinarian=self.veterinarian,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(id=self.id) 
        
        if overlapping_schedules.exists():
            raise ValueError("This time slot is already occupied.")

        super().save(*args, **kwargs)