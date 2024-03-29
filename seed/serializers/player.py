"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Player
from app.models import Team
from app.models import PlayerPosition
from app.models import File
from seed.serializers.file import FileSerializer

class PlayerSerializer(serializers.ModelSerializer):
    
    photo = FileSerializer(read_only=True)

    team_id = serializers.PrimaryKeyRelatedField(
        source='team', queryset=Team.objects.all(),
        required=True, allow_null=False)
    position_id = serializers.PrimaryKeyRelatedField(
        source='position', queryset=PlayerPosition.objects.all(),
        required=True, allow_null=False)
    photo_id = serializers.PrimaryKeyRelatedField(
        source='photo', queryset=File.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Player
        fields = (
            'id',
            'created_at',
            'hash',
            'name',
            'photo',
            'is_active',
            'photo_id',
            'team_id',
            'position_id',  
        )