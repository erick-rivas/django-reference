from rest_framework import viewsets

from models.match import Match
from serializers.match import MatchSerializer

class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
