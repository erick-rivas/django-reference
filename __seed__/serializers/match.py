"""
__Seed builder__v1.0
  (Read_only) Modify via models.json
"""

from rest_framework import serializers
from models.match import Match
from models.team import Team
from models.score import Score
from serializers.user import UserSerializer

class _MatchSerializer(serializers.ModelSerializer):  #
    
    class LocalSerializer(serializers.ModelSerializer):
        class Meta:
            model = Team
            fields ='__all__'
            depth = 0
    
    class VisitorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Team
            fields ='__all__'
            depth = 0
    
    class ScoresSerializer(serializers.ModelSerializer):
        class Meta:
            model = Score
            fields ='__all__'
            depth = 0
    
    local = LocalSerializer(read_only=True)
    visitor = VisitorSerializer(read_only=True)
    scores = ScoresSerializer(many=True,read_only=True)
    
    local_id = serializers.PrimaryKeyRelatedField(source='local', 
    	queryset=Team.objects.all(), write_only=True)
    visitor_id = serializers.PrimaryKeyRelatedField(source='visitor', 
    	queryset=Team.objects.all(), write_only=True)
    
    class Meta:
        model = Match
        fields = (
            'id',
            'date',
            'type',
            'local',
            'visitor',
            'scores',
            'local_id',
            'visitor_id',
        )
        depth = 1

