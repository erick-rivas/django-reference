"""
__Seed builder__v1.0

  Guidelines:
    - Add business logic via domains
    - Only override mentioned methods

  Override methods:
    - filter_queryset(self, queryset)
    - perform_create(self, serializer)
    - perform_update(self, serializer)
    - perform_destroy(self, instance)
"""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from __seed__.views.scores import _ScoreViewSet
from models.score import Score

class ScoreViewSet(_ScoreViewSet): #
    pass
