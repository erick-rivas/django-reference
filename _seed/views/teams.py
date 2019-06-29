"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from views.helpers.viewsets import FullViewSet

from models.team import Team
from serializers.team import TeamSerializer

class _TeamViewSet(FullViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
