from rest_framework import viewsets

from models.team import Team
from serializers.team import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()