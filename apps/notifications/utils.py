from push_notifications.models import GCMDevice

def send_push_notification(user, title, message):
    devices = GCMDevice.objects.filter(user=user)
    if devices.exists():
        devices.send_message(message, title=title)
