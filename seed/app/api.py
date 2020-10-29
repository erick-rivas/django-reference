"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.urls import path, include
from django.conf.urls import url
from dynamic_rest.routers import DynamicRouter

from app.views import MatchViewSet
from app.views import PlayerViewSet
from app.views import PlayerPositionViewSet
from app.views import ScoreViewSet
from app.views import TeamViewSet
from app.views import UserViewSet
from app.views import FileView

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