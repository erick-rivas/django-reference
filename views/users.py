"""
__Seed builder__v1.0

  Guidelines:
    - Add business logic via domains
    - Only override mentioned methods and actions
    - Reference: https://www.django-rest-framework.org/api-guide/viewsets/

  Override methods:
    - filter_queryset(self, queryset)
    - perform_create(self, serializer)
    - perform_update(self, serializer)
    - perform_destroy(self, instance)
    - Reference: https://www.django-rest-framework.org/api-guide/generic-views/#methods

  Override attributes:
    - access_class 
      - Inherit from permissions.BasePermission
      - Reference: https://www.django-rest-framework.org/api-guide/permissions/

  Action template:
    @action(detail=True|False, methods=['method_name'])
    def action_name(self, request, pk=None):
    - Reference: https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions
"""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from domain.helpers.query_util import _get, _list, _list_q, _list_o, _queryset, _create

from _seed.views.users import _UserViewSet
from models.user import User

class UserViewSet(_UserViewSet):  #
    pass

