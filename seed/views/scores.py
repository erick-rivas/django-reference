"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import Score
from app.serializers import ScoreSerializer

class _ScoreViewSet(ViewSet):  #

    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
