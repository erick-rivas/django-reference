"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Score
from app.models import Player
from app.models import Match

class ScoreSerializer(serializers.ModelSerializer):

    player_id = serializers.PrimaryKeyRelatedField(
        source='player', queryset=Player.objects.all(),
        required=True, allow_null=False)
    match_id = serializers.PrimaryKeyRelatedField(
        source='match', queryset=Match.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Score
        fields = (
            'id',
            'created_at',
            'hash',
            'min',
            'player_id',
            'match_id',  
        )