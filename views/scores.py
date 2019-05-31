"""
__Seed builder__v1.0
"""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from __seed__.views.scores import _ScoreViewSet
from models.score import Score

class ScoreViewSet(_ScoreViewSet):
    pass
