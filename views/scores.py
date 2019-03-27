from rest_framework import viewsets

from models.score import Score
from serializers.score import ScoreSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()