"""
__Seed builder__v1.0
  (Read_only) Modify via models.json
"""

from rest_framework import serializers
from serializers.helpers.serializer import Serializer
from models.player import Player
from models.team import Team
from serializers.user import UserSerializer

class _PlayerSerializer(Serializer):  #
    
    class TeamSerializer(Serializer):
        class Meta(Serializer.Meta):
            model = Team
    
    team = TeamSerializer(read_only=True)
    
    team_id = serializers.PrimaryKeyRelatedField(source='team', queryset=Team.objects.all())
    
    class Meta:
        model = Player
        fields = (
            'id',
            'hash',
            'name',
            'photo_url',
            'is_active',
            'team',
            'team_id',
        )
        depth = 1

