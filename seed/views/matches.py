"""
__Seed builder__v0.1.7
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import Match
from app.serializers import MatchSerializer

class _MatchViewSet(ViewSet):  #

    serializer_class = MatchSerializer
    queryset = Match.objects.all()
