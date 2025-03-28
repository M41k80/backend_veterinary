import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from apps.users.models import User
from asgiref.sync import sync_to_async

class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.veterinarian = self.scope['user']
        self.room_name = f'veterinarian_{self.veterinarian.id}'
        self.room_group_name = f'chat_{self.room_name}'
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        sender = self.scope['user']
        receiver = self.veterinarian
        await sync_to_async(self.save_message)(sender, receiver, message)
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message,
        }))
        
    @sync_to_async
    def save_message(self, sender, receiver, content):
        Message.objects.create(sender=sender, receiver=receiver, content=content)