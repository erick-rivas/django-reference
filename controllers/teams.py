from rest_framework import generics

from models.teams import Team
from models.serializers.teams import TeamSerializer


class GetTeamList(generics.ListAPIView):
    serializer_class = TeamSerializer
    def get_queryset(self):
        queryset = Team.objects.all()
        return queryset

class GetTeamDetails(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer