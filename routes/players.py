from routes.helpers.viewsets import FullViewSet
from models.player import Player
from models.serializers.player import PlayerSerializer

class PlayerViewSet(FullViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
