from rest_framework import serializers
from models.team import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'logo_url', 'players')
        depth = 1
