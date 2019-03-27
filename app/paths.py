from django.urls import path, include
from rest_framework.routers import DefaultRouter

from views.matches import MatchViewSet
from views.players import PlayerViewSet
from views.scores import ScoreViewSet
from views.teams import TeamViewSet


router = DefaultRouter()
router.register(r'matches', MatchViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'scores', ScoreViewSet)
router.register(r'teams', TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]