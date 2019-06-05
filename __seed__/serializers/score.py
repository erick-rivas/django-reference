"""
__Seed builder__v1.0
  (Read_only) Modify via models.json
"""

from rest_framework import serializers
from models.score import Score
from models.player import Player
from models.match import Match
from serializers.user import UserSerializer

class _ScoreSerializer(serializers.ModelSerializer):  #
    
    class PlayerSerializer(serializers.ModelSerializer):
        class Meta:
            model = Player
            fields ='__all__'
            depth = 0
    
    class MatchSerializer(serializers.ModelSerializer):
        class Meta:
            model = Match
            fields ='__all__'
            depth = 0
    
    player = PlayerSerializer(read_only=True)
    match = MatchSerializer(read_only=True)
    
    player_id = serializers.PrimaryKeyRelatedField(source='player', queryset=Player.objects.all())
    match_id = serializers.PrimaryKeyRelatedField(source='match', queryset=Match.objects.all())
    
    class Meta:
        model = Score
        fields = (
            'id',
            'min',
            'player',
            'match',
            'player_id',
            'match_id',
        )
        depth = 1
