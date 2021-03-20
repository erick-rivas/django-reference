"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import User
from app.models import Team

class _UserSerializer(serializers.ModelSerializer):

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
            'team_ids',  
        )