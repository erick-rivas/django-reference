"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from app.models import Player
from app.models import Team
from app.models import PlayerType
from app.models import File
from seed.serializers.helpers.file import FileSerializer

from dynamic_rest.fields import DynamicRelationField

class _PlayerSerializer(Serializer):  #
    
    team = DynamicRelationField('app.serializers.TeamSerializer', 
        deferred=True, embed=True, read_only=True)
    type = DynamicRelationField('app.serializers.PlayerTypeSerializer', 
        deferred=True, embed=True, read_only=True)
    photo = FileSerializer(read_only=True)

    team_id = serializers.PrimaryKeyRelatedField(source='team', queryset=Team.objects.all(), 
        required=True, allow_null=False)
    type_id = serializers.PrimaryKeyRelatedField(source='type', queryset=PlayerType.objects.all(), 
        required=True, allow_null=False)
    photo_id = serializers.PrimaryKeyRelatedField(source='photo', queryset=File.objects.all(), 
        required=True, allow_null=False)

    class Meta:
        model = Player
        fields = (
            'id',
            'hash',
            'name',
            'photo',
            'is_active',
            'team',
            'type',
            'photo_id',
            'team_id',
            'type_id',  
        )
