"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Player
from app.serializers import PlayerSerializer

class PlayerViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Player.filter_permissions(
            super().get_queryset(), Player.permission_filters(user))