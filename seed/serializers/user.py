"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from app.models import User
from app.models import Team
from app.models import File
from seed.serializers.helpers.file import FileSerializer

from dynamic_rest.fields import DynamicRelationField

class _UserSerializer(Serializer):  #
    
    teams = DynamicRelationField('serializers.team.TeamSerializer', 
        deferred=True, embed=True, many=True, read_only=True)

    team_ids = serializers.PrimaryKeyRelatedField(many=True, source='teams', read_only=True)

    class Meta:
        model = User
        extra_fields = ()
        default_fields = (
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
        fields = default_fields + extra_fields
