"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import Player
from app.serializers import PlayerSerializer

class _PlayerViewSet(ViewSet):  #

    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
