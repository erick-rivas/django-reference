"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Team
from app.models import File
from seed.serializers.helpers.file import FileSerializer

class _TeamSerializer(serializers.ModelSerializer):
    
    logo = FileSerializer(read_only=True)
    identity_docs = FileSerializer(many=True, read_only=True)

    player_ids = serializers.PrimaryKeyRelatedField(many=True, source='players', read_only=True)
    identity_doc_ids = serializers.PrimaryKeyRelatedField(many=True, source='identity_docs', read_only=True)

    rival_id = serializers.PrimaryKeyRelatedField(source='rival', queryset=Team.objects.all(), 
        required=False, allow_null=True)
    logo_id = serializers.PrimaryKeyRelatedField(source='logo', queryset=File.objects.all(), 
        required=True, allow_null=False)

    class Meta:
        model = Team
        fields = (
            'id',
            'hash',
            'name',
            'logo',
            'description',
            'market_value',
            'identity_docs',
            'logo_id',
            'identity_doc_ids',
            'rival_id',
            'player_ids',  
        )