from django.urls import path
from team.views import GetTeamList, GetTeamDetails

urlpatterns = [
    path('teams/', GetTeamList.as_view()),
    path('teams/<int:pk>', GetTeamDetails.as_view())
]
