"""
__Seed builder__v1.0
"""

from views.helpers.viewsets import FullViewSet

from models.match import Match
from serializers.match import MatchSerializer

class _MatchViewSet(FullViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
