from django.urls import path
from player.views import GetPlayerList, GetPlayerDetails

urlpatterns = [
    path('players/', GetPlayerList.as_view()),
    path('players/<int:pk>', GetPlayerDetails.as_view())
]
