"""
__Seed builder__v0.1.8
  (Read_only) Builder helper
"""

import os
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import viewsets
from dynamic_rest.viewsets import WithDynamicViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

class ViewSet(WithDynamicViewSetMixin, viewsets.ModelViewSet):  #

    def get_serializer(self, *args, **kwargs):
        kwargs['envelope'] = False
        return super(ViewSet, self).get_serializer(*args, **kwargs)

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