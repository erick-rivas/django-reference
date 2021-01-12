"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.helpers.viewsets import ViewSet
from app.models import User
from app.serializers import UserSerializer

class _UserViewSet(ViewSet,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
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