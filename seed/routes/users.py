"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import User
from app.serializers import UserSerializer

class UserViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get_queryset(self):
        user = self.request.user
        return User.filter_permissions(
            super().get_queryset(), User.permission_filters(user))