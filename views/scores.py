from views.viewset import ViewSet
from models.score import Score
from serializers.score import ScoreSerializer

class ScoreViewSet(ViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
