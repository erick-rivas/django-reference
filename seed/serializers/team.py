"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from models.team import Team
from models.player import Player
from models.helpers.file import File

from serializers.helpers.file import FileSerializer
from dynamic_rest.fields import DynamicRelationField

class _TeamSerializer(Serializer):  #
    
    rival = DynamicRelationField('serializers.team.TeamSerializer', 
        deferred=True, embed=True, read_only=True)
    players = DynamicRelationField('serializers.player.PlayerSerializer', 
        deferred=True, embed=True, many=True, read_only=True)
    logo = FileSerializer(read_only=True)
    identity_docs = FileSerializer(many=True, read_only=True)

    player_ids = serializers.PrimaryKeyRelatedField(many=True, source='players', read_only=True)
    identity_doc_ids = serializers.PrimaryKeyRelatedField(many=True, source='identity_docs', read_only=True)

    rival_id = serializers.PrimaryKeyRelatedField(source='rival', queryset=Team.objects.all(), 
        required=False, allow_null=True)
    logo_id = serializers.PrimaryKeyRelatedField(source='logo', queryset=File.objects.all(), 
        required=True, allow_null=False)

    class Meta:
        model = Team
        fields = (
            'id',
            'hash',
            'name',
            'logo',
            'description',
            'market_value',
            'rival',
            'identity_docs',
            'players',
            'logo_id',
            'identity_doc_ids',
            'rival_id',
            'player_ids',  
        )
