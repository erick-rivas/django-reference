from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from views.matches import MatchViewSet
from views.players import PlayerViewSet
from views.scores import ScoreViewSet
from views.teams import TeamViewSet
from views.users import UserViewSet

router = DefaultRouter()
router.register(r'matches', MatchViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'scores', ScoreViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls'))
]
