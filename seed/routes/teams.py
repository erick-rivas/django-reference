"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Team
from app.serializers import TeamSerializer

class TeamViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Team.filter_permissions(
            super().get_queryset(), Team.permission_filters(user))