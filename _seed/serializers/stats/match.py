"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from rest_framework import serializers
from serializers.helpers.serializer import Serializer
from serializers.helpers.serializer import InnerSerializer
from models.stats.match import Match
from models.team import Team
from models.stats.score import Score
from models.helpers.file import File
from serializers.user import UserSerializer
from serializers.helpers.file import FileSerializer

class _MatchSerializer(Serializer):  #
    
    local = InnerSerializer(Team, read_only=True)
    visitor = InnerSerializer(Team, read_only=True)
    scores = InnerSerializer(Score, many=True, read_only=True)

    local_id = serializers.PrimaryKeyRelatedField(source='local', queryset=Team.objects.all())
    visitor_id = serializers.PrimaryKeyRelatedField(source='visitor', queryset=Team.objects.all())

    score_ids = serializers.PrimaryKeyRelatedField(many=True, source='scores', read_only=True)
    
    class Meta:
        model = Match
        fields = (
            'id',
            'hash',
            'date',
            'type',
            'local',
            'visitor',
            'scores',
            'local_id',
            'visitor_id',
            'score_ids',  
        )

