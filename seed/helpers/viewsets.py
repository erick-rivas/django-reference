"""
__Seed builder__v0.2.0
  (Read_only) Builder helper
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from dynamic_rest.viewsets import WithDynamicViewSetMixin
from django.shortcuts import get_object_or_404
from app.settings import get_env


class ViewSet(WithDynamicViewSetMixin):

    if get_env('ENABLE_AUTH'):
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated, )

    def get_serializer(self, *args, **kwargs):
        kwargs['envelope'] = False
        return super(ViewSet, self).get_serializer(*args, **kwargs)