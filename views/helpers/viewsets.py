import os
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions


class BaseViewSet(viewsets.GenericViewSet):  #

    class AccessPermission(permissions.BasePermission):
        pass

    if 'ENABLE_SECURITY' in os.environ:
        authentication_classes = (TokenAuthentication,)
        access_class = AccessPermission
        permission_classes = (IsAuthenticated, access_class)

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

class ReadOnlyViewSet(
    BaseViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin):
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_fields = '__all__'
    ordering_fields = '__all__'

class WriteOnlyViewSet(
    BaseViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin):
    pass

class ReadWriteViewSet(
    ReadOnlyViewSet,
    WriteOnlyViewSet):
    pass

class WriteDeleteViewSet(
    WriteOnlyViewSet,
    mixins.DestroyModelMixin):
    pass

class FullViewSet(
    ReadWriteViewSet,
    mixins.DestroyModelMixin):
    pass
