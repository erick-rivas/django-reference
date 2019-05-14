from routes.helpers.viewsets import FullViewSet
from models.team import Team
from models.serializers.team import TeamSerializer

class TeamViewSet(FullViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
