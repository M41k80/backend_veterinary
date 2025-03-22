from django.db import models
from apps.users.models import User

class Appointment(models.Model):
    pet = models.CharField(max_length=255)
    veterinarian = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments', limit_choices_to={'is_veterinarian': True})
    date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'),('completed', 'Completed'), ('cancelled', 'Cancelled'), ('rescheduled', 'Rescheduled')], default='pending')
    services = models.ManyToManyField('services.Service', related_name='appointments')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def calculate_total_cost(self):
        self.total_cost = sum(service.price for service in self.services.all())
        self.save()
        
    
    def __str__(self):
        return f"Appointment for {self.pet} on {self.date} by {self.veterinarian.username}"
    
