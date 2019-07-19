"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from app.models import Team
from app.models import Player
from app.models import File
from seed.serializers.helpers.file import FileSerializer

from dynamic_rest.fields import DynamicRelationField

class _TeamSerializer(Serializer):  #
    
    rival = DynamicRelationField('app.serializers.TeamSerializer', 
        deferred=True, embed=True, read_only=True)
    players = DynamicRelationField('app.serializers.PlayerSerializer',deferred=True, embed=True, many=True, read_only=True)
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
        extra_fields = ()
        default_fields = (
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
        fields = default_fields + extra_fields
