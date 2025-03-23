from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'timestamp', 'is_read']
        read_only_fields = ['timestamp'] 
        
    def validate(self, data):
        sender = data.get('sender')
        receiver = data.get('receiver')

    
        if sender.role != 'pet_owner':
            raise serializers.ValidationError("only pet owners can send messages.")
    
        if receiver.role != 'veterinarian':
            raise serializers.ValidationError("only veterinarians can receive messages.")

        return data