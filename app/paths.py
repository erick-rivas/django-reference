from django.urls import path
from controllers.matches import GetMatchList, GetMatchDetails
from controllers.players import GetPlayerList, GetPlayerDetails
from controllers.scores import SaveScore
from controllers.teams import GetTeamList, GetTeamDetails

urlpatterns = [
    path('matches/', GetMatchList.as_view()),
    path('matches/<int:pk>', GetMatchDetails.as_view()),
    path('players/', GetPlayerList.as_view()),
    path('players/<int:pk>', GetPlayerDetails.as_view()),
    path('scores/', SaveScore.as_view()),
    path('teams/', GetTeamList.as_view()),
    path('teams/<int:pk>', GetTeamDetails.as_view())
]
