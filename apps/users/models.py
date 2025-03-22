from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('veterinarian', 'Veterinarian'),
        ('receptionist', 'Receptionist'),
        ('pet_owner', 'Pet Owner'),
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='pet_owner')