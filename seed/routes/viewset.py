"""
__Seed builder__v0.2.0
  (Read_only) Builder helper
"""

from app.settings import get_env
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ViewSet:
    if get_env('ENABLE_AUTH'):
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)

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