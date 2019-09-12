"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import PlayerType
from app.serializers import PlayerTypeSerializer

class _PlayerTypeViewSet(ViewSet):  #

    serializer_class = PlayerTypeSerializer
    queryset = PlayerType.objects.all()
