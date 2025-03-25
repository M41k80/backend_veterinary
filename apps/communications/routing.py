from django.urls import re_path
from .consumers import MessageConsumer

websocket_urlpatterns = [
    re_path(r'ws/messages/(?P<veterinarian_id>\d+)/$', MessageConsumer.as_asgi()),
]


#Si quieres manejar los WebSockets en el frontend (por ejemplo, en React), puedes hacer una conexión WebSocket a la URL ws://localhost:8000/ws/messages/{veterinarian_id}/ cuando el veterinario se conecte a la aplicación.