from rest_framework import generics
from rest_framework.response import Response

from player.models import Player
from player.serializer import PlayersSerializer



class PlayersView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayersSerializer

class PlayerView(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayersSerializer