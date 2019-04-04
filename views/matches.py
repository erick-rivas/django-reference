from views.viewset import ViewSet
from models.match import Match
from serializers.match import MatchSerializer

class MatchViewSet(ViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
