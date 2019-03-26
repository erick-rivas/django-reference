from rest_framework import generics

from models.players import Player
from models.serializers.players import PlayerSerializer


class GetPlayerList(generics.ListAPIView):
    serializer_class = PlayerSerializer
    def get_queryset(self):
        queryset = Player.objects.all()
        return queryset

class GetPlayerDetails(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer