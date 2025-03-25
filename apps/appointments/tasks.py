from celery import shared_task
from django.core.mail import send_mail
from .models import Appointment
from django.utils import timezone

@shared_task
def send_appointment_reminders():
    today = timezone.now()
    
    appointments = Appointment.objects.filter(
        reminder_date__lte=today,
        reminder_sent=False
    )

    for appointment in appointments:
       
        send_mail(
            subject='Reminder: Your pet has an appointment',
            message=f"Hello, the appoinment for {appointment.pet.name} with the veterinarian {appointment.veterinarian.username} is tomorrow at: {appointment.start_time.strftime('%H:%M')}.",
            from_email='vetclinicapiv1@gmail.com',
            recipient_list=[appointment.pet.owner.email],
        )
        
       
        appointment.reminder_sent = True
        appointment.save()

    return f"{len(appointments)} reminders sent."
