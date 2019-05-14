from routes.helpers.viewsets import FullViewSet
from models.score import Score
from models.serializers.score import ScoreSerializer

class ScoreViewSet(FullViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
