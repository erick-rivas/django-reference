"""
__Seed builder__v1.0
  (Read_only) Modify via models.json
"""

from rest_framework import serializers
from serializers.helpers.serializer import Serializer
from models.user import User
from models.team import Team

class _UserSerializer(Serializer):  #
    
    class TeamsSerializer(Serializer):
        class Meta(Serializer.Meta):
            model = Team
    
    teams = TeamsSerializer(many=True, read_only=True)
    
    team_ids = serializers.PrimaryKeyRelatedField(many=True, source='teams', read_only=True)
    
    class Meta:
        model = User
        fields = (
            'id',
            'hash',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'teams',
            'team_ids',
        )
        depth = 1

