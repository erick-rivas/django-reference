"""
__Seed builder__v1.0

  Base routes:
    - /matches
    - /players
    - /player_types
    - /scores
    - /teams
    - /users
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
