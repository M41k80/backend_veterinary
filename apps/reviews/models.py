from django.db import models
from apps.users.models import User
from apps.appointments.models import Appointment

class Rating(models.Model):
    veterinarian = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'veterinarian'}, related_name='veterinarian_ratings')
    pet_owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'pet_owner'}, related_name='pet_owner_ratings')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comment = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating for {self.veterinarian.username} by {self.pet_owner.username} on {self.timestamp}"
