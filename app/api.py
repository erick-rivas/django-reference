"""
__Seed builder__v1.0
  Routes:
    - /users
    - /teams
    - /players
    - /matches
    - /scores
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
