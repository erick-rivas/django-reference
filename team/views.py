from rest_framework import generics

from team.models import Team
from team.serializer import TeamSerializer


class GetTeamList(generics.ListAPIView):
    serializer_class = TeamSerializer
    def get_queryset(self):
        queryset = Team.objects.all()
        return queryset

class GetTeamDetails(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer