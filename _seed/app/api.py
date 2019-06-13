"""
__Seed builder__v1.0
  (Read_only) Modify via models.json
"""

from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from views.users import UserViewSet
from views.teams import TeamViewSet
from views.players import PlayerViewSet
from views.matches import MatchViewSet
from views.scores import ScoreViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'scores', ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls'))
]