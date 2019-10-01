"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from app.models import Player
from app.models import Team
from app.models import PlayerPosition
from app.models import File
from seed.serializers.helpers.file import FileSerializer

from dynamic_rest.fields import DynamicRelationField

class _PlayerSerializer(Serializer):  #
    
    team = DynamicRelationField('app.serializers.TeamSerializer', 
        deferred=True, embed=True, read_only=True)
    position = DynamicRelationField('app.serializers.PlayerPositionSerializer', 
        deferred=True, embed=True, read_only=True)
    photo = FileSerializer(read_only=True)

    team_id = serializers.PrimaryKeyRelatedField(source='team', queryset=Team.objects.all(), 
        required=True, allow_null=False)
    position_id = serializers.PrimaryKeyRelatedField(source='position', queryset=PlayerPosition.objects.all(), 
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
            'position',
            'photo_id',
            'team_id',
            'position_id',  
        )
