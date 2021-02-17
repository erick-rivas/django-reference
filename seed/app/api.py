"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.urls import path, include
from django.conf.urls import url
from dynamic_rest.routers import DynamicRouter

from app.routes import MatchViewSet
from app.routes import PlayerViewSet
from app.routes import PlayerPositionViewSet
from app.routes import ScoreViewSet
from app.routes import TeamViewSet
from app.routes import UserViewSet
from app.routes import FileView

router = DynamicRouter()
router.register(r'matches', MatchViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'player_positions', PlayerPositionViewSet)
router.register(r'scores', ScoreViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('files/', FileView.as_view()),
    url(r'^auth/', include('rest_auth.urls'))
]