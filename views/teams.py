"""
__Seed builder__v1.0
"""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.req_util import has_fields_or_400
from seed.util.query_util import _get, _list, _list_q, _list_o, _queryset, _create

from seed.views.teams import _TeamViewSet
from app.models import Team

class TeamViewSet(_TeamViewSet):  #
    pass
