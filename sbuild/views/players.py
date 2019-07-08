"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from sbuild.helpers.viewsets import ViewSet

from models.player import Player
from serializers.player import PlayerSerializer

class _PlayerViewSet(ViewSet):  #

    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
