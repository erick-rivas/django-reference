from rest_framework import serializers
from models.serializers.helpers.util import Util
from models.player import Player
from models.match import Match
from models.score import Score

class ScoreSerializer(serializers.ModelSerializer):
    player_id = serializers.PrimaryKeyRelatedField(source='player', queryset=Player.objects.all(), write_only=True)
    match_id = serializers.PrimaryKeyRelatedField(source='match', queryset=Match.objects.all(), write_only=True)
    class Meta:
        model = Score
        fields = Util.get_attr_list(Score,
            include=('player_id', 'match_id'))
        depth = 1
