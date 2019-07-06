"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from views.helpers.viewsets import FullViewSet

from models.stat.match import Match
from serializers.stat.match import MatchSerializer

class _MatchViewSet(FullViewSet):  #

    serializer_class = MatchSerializer
    queryset = Match.objects.all()
