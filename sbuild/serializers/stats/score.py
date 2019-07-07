"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from rest_framework import serializers
from serializers.helpers.serializer import Serializer
from serializers.helpers.serializer import InnerSerializer
from models.stats.score import Score
from models.player import Player
from models.stats.match import Match
from models.helpers.file import File

from serializers.helpers.file import FileSerializer
from dynamic_rest.fields import DynamicRelationField

class _ScoreSerializer(Serializer):  #
    
    player = DynamicRelationField('serializers.player.PlayerSerializer', 
        deferred=True, embed=True, read_only=True)
    match = DynamicRelationField('serializers.stats.match.MatchSerializer', 
        deferred=True, embed=True, read_only=True)

    player_id = serializers.PrimaryKeyRelatedField(source='player', queryset=Player.objects.all(), 
        required=True, allow_null=False)
    match_id = serializers.PrimaryKeyRelatedField(source='match', queryset=Match.objects.all(), 
        required=True, allow_null=False)

    class Meta:
        model = Score
        fields = (
            'id',
            'hash',
            'min',
            'player',
            'match',
            'player_id',
            'match_id',  
        )