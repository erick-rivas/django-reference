from rest_framework import serializers

from models.match import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'date', 'local', 'visitor', 'scores')
        depth = 1

