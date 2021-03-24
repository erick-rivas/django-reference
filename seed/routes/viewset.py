"""
__Seed builder__v0.2.0
  (Read_only) Builder helper
"""

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from app.settings import get_env


class ViewSet:
    if get_env('ENABLE_AUTH'):
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated, )