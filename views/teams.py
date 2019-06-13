"""
__Seed builder__v1.0

  Guidelines:
    - Add business logic via domains
    - Only override mentioned methods and actions

  Override methods:
    - filter_queryset(self, queryset)
    - perform_create(self, serializer)
    - perform_update(self, serializer)
    - perform_destroy(self, instance)

  Override classes:
    - AccessPermission(permissions.BasePermission):

  Action template:
    @action(detail=True|False, methods=['method_name'])
    def action_name(self, request, pk=None):
"""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404

from _seed.views.teams import _TeamViewSet
from models.team import Team

class TeamViewSet(_TeamViewSet): #
    pass
