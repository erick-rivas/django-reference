"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from rest_framework import serializers
from serializers.helpers.serializer import Serializer
from serializers.helpers.serializer import InnerSerializer
from models.player import Player
from models.team import Team
from models.helpers.file import File
from serializers.user import UserSerializer
from serializers.helpers.file import FileSerializer

class _PlayerSerializer(Serializer):  #
    
    team = InnerSerializer(Team, read_only=True)
    photo = FileSerializer(read_only=True)

    team_id = serializers.PrimaryKeyRelatedField(source='team', queryset=Team.objects.all())
    photo_id = serializers.PrimaryKeyRelatedField(source='photo', queryset=File.objects.all())

    class Meta:
        model = Player
        fields = (
            'id',
            'hash',
            'name',
            'photo',
            'is_active',
            'team',
            'photo_id',
            'team_id',  
        )
