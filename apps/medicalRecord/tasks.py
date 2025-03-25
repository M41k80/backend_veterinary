from celery import shared_task
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone
from .models import MedicalRecord

@shared_task
def check_vaccine_reminders():
    today = timezone.now().date()
    reminder_days = timedelta(days=7) 

    
    records = MedicalRecord.objects.filter(
        next_vaccine_reminder__lte=today + reminder_days
    )

    for record in records:
        
        send_mail(
            subject='Vaccine reminder',
            message=f"Reminder: Your pet {record.pet.name} is due for a vaccine soon.",
            from_email='vetclinicapiv1@gmail.com',
            recipient_list=[record.pet.owner.email],
        )
