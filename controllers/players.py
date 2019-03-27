from rest_framework import generics

from models.player import Player
from models.serializers.player import PlayerSerializer


class GetPlayerList(generics.ListAPIView):
    serializer_class = PlayerSerializer
    def get_queryset(self):
        queryset = Player.objects.all()
        team_id = self.request.query_params.get('team_id', None)
        if team_id is not None:
            queryset = queryset.filter(team__id=team_id)
        return queryset

class GetPlayerDetails(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer