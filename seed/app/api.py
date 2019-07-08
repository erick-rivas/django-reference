"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from django.urls import path, include
from django.conf.urls import url
from dynamic_rest.routers import DynamicRouter

from views.players import PlayerViewSet
from views.teams import TeamViewSet
from views.users import UserViewSet
from views.stats.matches import MatchViewSet
from views.stats.scores import ScoreViewSet
from seed.helpers.file_view import FileView

router = DynamicRouter()
router.register(r'players', PlayerViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'scores', ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('files/', FileView.as_view()),
    url(r'^auth/', include('rest_auth.urls'))
]
