from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from seed.app.asgi import BaseSocket

async def send_ws_message(room, data):
    channel_layers = get_channel_layer()
    await channel_layers.group_send(
        room,
        {
            "type": "send_message",
            "message": data
        }
    )

def send_global_message(data):
    async_to_sync(send_ws_message)(BaseSocket.room, data)