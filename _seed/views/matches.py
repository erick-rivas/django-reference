"""
__Seed builder__v1.0
  (Read_only) Modify via models.json
"""

from views.helpers.viewsets import FullViewSet

from models.match import Match
from serializers.match import MatchSerializer

class _MatchViewSet(FullViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
