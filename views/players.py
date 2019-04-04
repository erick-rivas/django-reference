from views.viewset import ViewSet
from models.player import Player
from serializers.player import PlayerSerializer

class PlayerViewSet(ViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
