from rest_framework import serializers

from models.serializers.players import PlayerSerializer
from models.teams import Team

class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)
    class Meta:
        model = Team
        fields = ('id', 'name', 'logo_url', 'players.py')
