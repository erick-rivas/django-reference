"""
__Seed builder__v1.0
  (Read_only) Modify via SeedManifest.yaml
"""

from rest_framework import serializers
from serializers.helpers.serializer import Serializer
from models.match import Match
from models.team import Team
from models.score import Score
from serializers.user import UserSerializer

class _MatchSerializer(Serializer):  #
    
    class LocalSerializer(Serializer):
        class Meta(Serializer.Meta):
            model = Team
    
    class VisitorSerializer(Serializer):
        class Meta(Serializer.Meta):
            model = Team
    
    class ScoresSerializer(Serializer):
        class Meta(Serializer.Meta):
            model = Score
    
    local = LocalSerializer(read_only=True)
    visitor = VisitorSerializer(read_only=True)
    scores = ScoresSerializer(many=True, read_only=True)
    
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
        depth = 1

