from views.viewset import ViewSet
from models.team import Team
from serializers.team import TeamSerializer

class TeamViewSet(ViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
