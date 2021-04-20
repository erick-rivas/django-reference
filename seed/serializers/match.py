"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Match
from app.models import Team

class MatchSerializer(serializers.ModelSerializer):

    score_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='scores', read_only=True)

    local_id = serializers.PrimaryKeyRelatedField(
        source='local', queryset=Team.objects.all(),
        required=True, allow_null=False)
    visitor_id = serializers.PrimaryKeyRelatedField(
        source='visitor', queryset=Team.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Match
        fields = (
            'id',
            'hash',
            'date',
            'type',
            'local_id',
            'visitor_id',
            'score_ids',  
        )