"""
__Seed builder__v1.0

  Guidelines:
    - Add business logic via domains
    - Preferably just add actions if required
    - Reference viewset: https://www.django-rest-framework.org/api-guide/viewsets/
    - Reference actions: reference: https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions

  Override attributes:
    - access_class 
      - Inherit from permissions.BasePermission
      - Reference: https://www.django-rest-framework.org/api-guide/permissions/
"""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from views.helpers.req_util import has_fields_or_400
from domain.helpers.query_util import _get, _list, _list_q, _list_o, _queryset, _create

from sbuild.views.stats.scores import _ScoreViewSet
from models.stats.score import Score

class ScoreViewSet(_ScoreViewSet):  #
    pass