from django.conf import settings
from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    pet_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pets', limit_choices_to={'is_pet_owner': True})

    def __str__(self):
        return f"{self.name} ({self.breed})"
