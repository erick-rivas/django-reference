from rest_framework import generics

from player.models import Player
from player.serializer import PlayerSerializer


class GetPlayerList(generics.ListAPIView):
    serializer_class = PlayerSerializer
    def get_queryset(self):
        queryset = Player.objects.all()
        return queryset

class GetPlayerDetails(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer