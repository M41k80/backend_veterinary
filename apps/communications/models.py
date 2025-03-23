from django.db import models
from apps.users.models import User  

class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        help_text="User that sends the message.",
        limit_choices_to={'role': 'pet_owner'}
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_messages',
        help_text="User that receives the message.",
        limit_choices_to={'role': 'veterinarian'}
    )
    content = models.TextField(help_text="Content of the message.")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="Timestamp of the message.")
    is_read = models.BooleanField(default=False, help_text="Whether the message has been read or not.")

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}"