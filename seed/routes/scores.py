"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Score
from app.serializers import ScoreSerializer

class ScoreViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Score.filter_permissions(
            super().get_queryset(), Score.permission_filters(user))