from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        
        user = self.request.user
        return Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)

    def perform_create(self, serializer):
        
        message = serializer.save(sender=self.request.user)
        
        
        send_mail(
            subject='New message from you from a pet owner',
            message=f'Hello, a new message from {message.sender.username} has been sent to you. the content is: {message.content}',
            from_email='vetclinicapiv1@gmail.com',
            recipient_list=[message.receiver.email],
        )