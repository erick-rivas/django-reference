"""
__Seed builder__v1.0

  Guidelines: 
    - Modify model routes via SeedManifest.yaml

  Routes:
    - /matches
    - /players
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
