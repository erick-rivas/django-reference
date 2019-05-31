"""
__Seed builder__v1.0
"""

from rest_framework import serializers
from models.team import Team
from models.player import Player
from serializers.user import UserSerializer

class _TeamSerializer(serializers.ModelSerializer):  #
    
    class PlayersSerializer(serializers.ModelSerializer):
        class Meta:
            model = Player
            fields ='__all__'
            depth = 0
    
    players = PlayersSerializer(many=True,read_only=True)
    
    
    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'logo_url',
            'description',
            'market_value',
            'players',
        )
        depth = 1

