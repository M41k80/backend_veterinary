from django.db import models
from apps.users.models import User
from push_notifications.models import GCMDevice

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(GCMDevice, on_delete=models.CASCADE)
