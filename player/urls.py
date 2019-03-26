from django.urls import path
from .views import PlayersView, PlayerView

urlpatterns = [
    path('players/', PlayersView.as_view()),
    path('players/<int:pk>/', PlayerView.as_view())
]