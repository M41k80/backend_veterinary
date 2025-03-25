from .utils import send_push_notification

def perform_create(self, serializer):
    message = serializer.save(sender=self.request.user)
    send_push_notification(
        user=message.receiver,
        title="New Message",
        message=f"You have a new message from {message.sender.username}"
    )
