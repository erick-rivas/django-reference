"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from rest_framework import serializers
from serializers.helpers.serializer import Serializer
from serializers.helpers.serializer import InnerSerializer
from models.user import User
from models.team import Team
from models.helpers.file import File
from serializers.helpers.file import FileSerializer

class _UserSerializer(Serializer):  #
    
    teams = InnerSerializer(Team, many=True, read_only=True)
    profile_image = FileSerializer(read_only=True)

    profile_image_id = serializers.PrimaryKeyRelatedField(source='profile_image', queryset=File.objects.all())

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
            'profile_image',
            'profile_image_id',
            'team_ids',  
        )

