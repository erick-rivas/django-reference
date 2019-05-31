"""
__Seed builder__v1.0
  Fields:
    - id
    - min
    - player
    - match
    - player_id
    - match_id
"""

from rest_framework import serializers
from __seed__.serializers.score import _ScoreSerializer

class ScoreSerializer(_ScoreSerializer):
    class PlayerSerializer(serializers.ModelSerializer):
        pass
    class MatchSerializer(serializers.ModelSerializer):
        pass

    class Meta(_ScoreSerializer.Meta):
        pass