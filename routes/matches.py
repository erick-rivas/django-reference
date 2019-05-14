from routes.helpers.viewsets import FullViewSet
from models.match import Match
from models.serializers.match import MatchSerializer

class MatchViewSet(FullViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
