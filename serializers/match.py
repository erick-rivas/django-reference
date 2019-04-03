from rest_framework import serializers
from models.match import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
        depth = 1
