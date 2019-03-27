from rest_framework import serializers

from models.score import Score

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'min', 'player', 'match')

    def create(self, validated_data):
        return Score.objects.create(**validated_data)
