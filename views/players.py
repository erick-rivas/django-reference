from rest_framework import viewsets

from models.player import Player
from serializers.player import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
