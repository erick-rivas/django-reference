"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from views.users import UserViewSet
from views.teams import TeamViewSet
from views.players import PlayerViewSet
from views.stats.matches import MatchViewSet
from views.stats.scores import ScoreViewSet
from views.helpers.files import FileView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'scores', ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('files/', FileView.as_view()),
    url(r'^auth/', include('rest_auth.urls'))
]