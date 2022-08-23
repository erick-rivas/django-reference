"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from urllib.parse import parse_qs

# pylint: disable=W0201
class BaseSocket(WebsocketConsumer):
    url = r'^ws/(?P<room>[^/]+)/$'

    def connect(self):
        self.room = self.scope['url_route']['kwargs']['room']
        self.params = parse_qs(self.scope['query_string'].decode('utf8'))
        async_to_sync(self.channel_layer.group_add)(
            self.room,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room,
            self.channel_name
        )

    def send_message(self, data):
        self.send(text_data=json.dumps(data["message"]))

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        URLRouter(
            [
                url(BaseSocket.url, BaseSocket.as_asgi())
            ]
        )
    )
})