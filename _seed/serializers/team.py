"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from rest_framework import serializers
from serializers.helpers.serializer import Serializer
from serializers.helpers.serializer import InnerSerializer
from models.team import Team
from models.player import Player
from models.helpers.file import File
from serializers.user import UserSerializer
from serializers.helpers.file import FileSerializer

class _TeamSerializer(Serializer):  #
    
    players = InnerSerializer(Player, many=True, read_only=True)
    logo = FileSerializer(read_only=True)
    identity_docs = FileSerializer(many=True, read_only=True)

    logo_id = serializers.PrimaryKeyRelatedField(source='logo', queryset=File.objects.all())

    player_ids = serializers.PrimaryKeyRelatedField(many=True, source='players', read_only=True)
    identity_doc_ids = serializers.PrimaryKeyRelatedField(many=True, source='identity_docs', read_only=True)
    
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
            'players',
            'logo_id',
            'identity_doc_ids',
            'player_ids',  
        )

