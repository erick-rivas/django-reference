"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from seed.helpers.viewsets import ViewSet

from models.stats.score import Score
from serializers.stats.score import ScoreSerializer

class _ScoreViewSet(ViewSet):  #

    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
