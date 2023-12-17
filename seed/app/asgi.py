"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json
from django.urls import re_path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from urllib.parse import parse_qs

connected = {}

# pylint: disable=W0201
class BaseSocket(WebsocketConsumer):
    url = r'^ws/(?P<room>[^/]+)/$'

    def connect(self):
        
        self.room = self.scope['url_route']['kwargs']['room']
        self.params = parse_qs(self.scope['query_string'].decode('utf8'))
        connected[self.room] = self.params

        async_to_sync(self.channel_layer.group_add)(
            self.room,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        connected.pop(self.room, None)
        async_to_sync(self.channel_layer.group_discard)(
            self.room,
            self.channel_name
        )

    def send_message(self, data):
        self.send(text_data=json.dumps(data["message"]))

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        URLRouter(
            [
                re_path(BaseSocket.url, BaseSocket.as_asgi())
            ]
        )
    )
})