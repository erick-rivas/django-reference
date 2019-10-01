"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import PlayerPosition
from app.serializers import PlayerPositionSerializer

class _PlayerPositionViewSet(ViewSet):  #

    serializer_class = PlayerPositionSerializer
    queryset = PlayerPosition.objects.all()
