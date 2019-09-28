"""
__Seed builder__v1.0
"""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.req_util import has_fields_or_400

from seed.views.users import _UserViewSet
from app.models import User

class UserViewSet(_UserViewSet):  #
    pass
