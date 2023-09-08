"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from app.routes import MatchViewSet
from app.routes import PlayerViewSet
from app.routes import PlayerPositionViewSet
from app.routes import ScoreViewSet
from app.routes import TeamViewSet
from app.routes import UserViewSet
from app.routes import FileView

router = DefaultRouter()
router.register(r'matches', MatchViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'player_positions', PlayerPositionViewSet)
router.register(r'scores', ScoreViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('files/', FileView.as_view()),
    re_path(r'^auth/', include('dj_rest_auth.urls'))
]