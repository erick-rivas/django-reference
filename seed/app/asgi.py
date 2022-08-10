from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class BaseSocket(WebsocketConsumer):

    url = r"^ws_global/$"
    room = "ws_global"

    def connect(self):
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

    # async def receive(self, text_data = None, bytes_data = None):
    #     pass

    def send_message(self, data):
        self.send(text_data=data["message"])

application = ProtocolTypeRouter({
  'websocket': AllowedHostsOriginValidator(
    URLRouter(
      [
        url(BaseSocket.url, BaseSocket.as_asgi())
      ]
    )
  )
})