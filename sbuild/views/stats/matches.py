"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from views.helpers.viewsets import FullViewSet

from models.stats.match import Match
from serializers.stats.match import MatchSerializer

class _MatchViewSet(FullViewSet):  #

    serializer_class = MatchSerializer
    queryset = Match.objects.all()
