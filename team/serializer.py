from rest_framework import serializers

from player.serializer import PlayerSerializer
from team.models import Team

class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)
    class Meta:
        model = Team
        fields = ('id', 'name', 'logo_url', 'players')
