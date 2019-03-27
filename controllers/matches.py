from rest_framework import generics
from django.db.models import Q

from models.match import Match
from models.serializers.match import MatchSerializer


class GetMatchList(generics.ListAPIView):
    serializer_class = MatchSerializer
    def get_queryset(self):
        queryset = Match.objects.all()
        team_id = self.request.query_params.get('team_id', None)
        if team_id is not None:
            queryset = queryset.filter(Q(local__id=team_id) | Q(visitor__id=team_id))
        return queryset

class GetMatchDetails(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer