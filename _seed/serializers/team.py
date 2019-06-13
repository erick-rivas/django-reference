"""
__Seed builder__v1.0
  (Read_only) Modify via models.json
"""

from rest_framework import serializers
from serializers.helpers.serializer import Serializer
from models.team import Team
from models.player import Player
from serializers.user import UserSerializer

class _TeamSerializer(Serializer):  #
    
    class PlayersSerializer(Serializer):
        class Meta(Serializer.Meta):
            model = Player
    
    players = PlayersSerializer(many=True, read_only=True)
    
    player_ids = serializers.PrimaryKeyRelatedField(many=True, source='players', read_only=True)
    
    class Meta:
        model = Team
        fields = (
            'id',
            'hash',
            'name',
            'logo_url',
            'description',
            'market_value',
            'players',
            'player_ids',
        )
        depth = 1

