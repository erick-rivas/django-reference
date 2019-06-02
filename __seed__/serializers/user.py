"""
__Seed builder__v1.0
  (Read_only) Modify via models.json
"""

from rest_framework import serializers
from models.user import User
from models.team import Team

class _UserSerializer(serializers.ModelSerializer):  #
    
    class TeamsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Team
            fields ='__all__'
            depth = 0
    
    teams = TeamsSerializer(many=True,read_only=True)
    
    
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'teams',
        )
        depth = 1

