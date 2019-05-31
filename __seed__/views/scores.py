"""
__Seed builder__v1.0
"""

from views.helpers.viewsets import FullViewSet

from models.score import Score
from serializers.score import ScoreSerializer

class _ScoreViewSet(FullViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
