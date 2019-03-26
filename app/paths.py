from django.urls import path
from controllers.players import GetPlayerList, GetPlayerDetails
from controllers.teams import GetTeamList, GetTeamDetails

urlpatterns = [
    path('players/', GetPlayerList.as_view()),
    path('players/<int:pk>', GetPlayerDetails.as_view()),
    path('teams/', GetTeamList.as_view()),
    path('teams/<int:pk>', GetTeamDetails.as_view())
]
