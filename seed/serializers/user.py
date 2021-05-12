"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import User
from app.models import Team
from app.models import File
from seed.serializers.file import FileSerializer

class UserSerializer(serializers.ModelSerializer):
    
    profile_image = FileSerializer(read_only=True)

    team_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='teams', queryset=Team.objects.all(),
        required=True, allow_null=False)
    profile_image_id = serializers.PrimaryKeyRelatedField(
        source='profile_image', queryset=File.objects.all(),
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
            'profile_image',
            'profile_image_id',
            'team_ids',  
        )