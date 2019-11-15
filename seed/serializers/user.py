"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from dynamic_rest.fields import DynamicRelationField
from app.models import User
from app.models import Team

class _UserSerializer(Serializer):  #
    
    teams = DynamicRelationField('app.serializers.TeamSerializer', 
        deferred=True, embed=True, many=True, read_only=True)

    team_ids = serializers.PrimaryKeyRelatedField(many=True, source='teams', queryset=Team.objects.all(), 
        required=True, allow_null=False)

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