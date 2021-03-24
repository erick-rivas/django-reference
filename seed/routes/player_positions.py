"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import PlayerPosition
from app.serializers import PlayerPositionSerializer

class _PlayerPositionViewSet(ViewSet,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    serializer_class = PlayerPositionSerializer
    queryset = PlayerPosition.objects.all()
    def destroy(self, request, pk=None):
        model = get_object_or_404(self.queryset, pk=pk)
        model.delete()
        return Response({'id': int(pk)}, status=status.HTTP_200_OK)
    def update(self, request, pk=None):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        return PlayerPosition.filter_permissions(super().get_queryset(), PlayerPosition.permission_filters(user))