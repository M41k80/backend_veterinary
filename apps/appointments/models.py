from django.db import models
from django.utils import timezone
from apps.users.models import User
import datetime


class Appointment(models.Model):
    pet = models.ForeignKey('pets.Pet', on_delete=models.CASCADE, related_name='appointments')
    veterinarian = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments', limit_choices_to={'role': 'veterinarian'})
    date = models.ForeignKey('schedules.Schedule', on_delete=models.CASCADE, related_name='appointments')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    reason = models.ForeignKey('services.Service', on_delete=models.CASCADE, related_name='appointments_reasons')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'),('completed', 'Completed'), ('cancelled', 'Cancelled'), ('rescheduled', 'Rescheduled')], default='pending')
    services = models.ManyToManyField('services.Service', related_name='appointments')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reminder_date = models.DateTimeField(blank=True, null=True)
    reminder_sent = models.BooleanField(default=False) 
    
    def save(self, *args, **kwargs):
        if not self.end_time:
            self.end_time = self.start_time + datetime.timedelta(minutes=30)
        
        if not self.schedule.is_available:
            raise ValueError("Selected schedule is not available.")
        
        overlapping_appointments = Appointment.objects.filter(
            veterinarian=self.veterinarian,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(id=self.id)
        
        if overlapping_appointments.exists():
            raise ValueError("This time slot is already occupied.")
        
        self.schedule.is_available = False
        self.schedule.save()
        
        self.reminder_date = self.start_time - datetime.timedelta(days=1)
        

        super().save(*args, **kwargs)
    
    def calculate_total_cost(self):
        self.total_cost = sum(service.price for service in self.services.all())
        self.save()
        
    
    def __str__(self):
        return f"Appointment for {self.pet} on {self.date} by {self.veterinarian.username}"
    
