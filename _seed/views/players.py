"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from views.helpers.viewsets import FullViewSet

from models.player import Player
from serializers.player import PlayerSerializer

class _PlayerViewSet(FullViewSet):  #

    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
