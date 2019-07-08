"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from sbuild.helpers.viewsets import ViewSet

from models.team import Team
from serializers.team import TeamSerializer

class _TeamViewSet(ViewSet):  #

    serializer_class = TeamSerializer
    queryset = Team.objects.all()
