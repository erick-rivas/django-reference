"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import PlayerPosition
from app.serializers import PlayerPositionSerializer

class PlayerPositionViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = PlayerPositionSerializer
    queryset = PlayerPosition.objects.all()
    def get_queryset(self):
        user = self.request.user
        return PlayerPosition.filter_permissions(
            super().get_queryset(), PlayerPosition.permission_filters(user))