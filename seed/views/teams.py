"""
__Seed builder__v0.1.7
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import Team
from app.serializers import TeamSerializer

class _TeamViewSet(ViewSet):  #

    serializer_class = TeamSerializer
    queryset = Team.objects.all()
