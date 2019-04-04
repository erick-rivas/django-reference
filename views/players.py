from views.helpers.viewsets import FullViewSet
from models.player import Player
from serializers.player import PlayerSerializer

class PlayerViewSet(FullViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
