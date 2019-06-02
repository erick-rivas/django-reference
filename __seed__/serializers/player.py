"""
__Seed builder__v1.0
  (Read_only) Modify via models.json
"""

from rest_framework import serializers
from models.player import Player
from models.team import Team
from serializers.user import UserSerializer

class _PlayerSerializer(serializers.ModelSerializer):  #
    
    class TeamSerializer(serializers.ModelSerializer):
        class Meta:
            model = Team
            fields ='__all__'
            depth = 0
    
    team = TeamSerializer(read_only=True)
    
    team_id = serializers.PrimaryKeyRelatedField(source='team', 
    	queryset=Team.objects.all(), write_only=True)
    
    class Meta:
        model = Player
        fields = (
            'id',
            'name',
            'photo_url',
            'is_active',
            'team',
            'team_id',
        )
        depth = 1

