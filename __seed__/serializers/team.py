"""
__Seed builder__v1.0
  (Read_only) Modify via models.json
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
    
    players = PlayersSerializer(many=True, read_only=True)
    
    player_ids = serializers.PrimaryKeyRelatedField(many=True, source='players', read_only=True)
    
    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'logo_url',
            'description',
            'market_value',
            'players',
            'player_ids',
        )
        depth = 1

