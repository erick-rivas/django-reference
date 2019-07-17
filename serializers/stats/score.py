"""
__Seed builder__v1.0

  Base fields:
    - id
    - min
    - player
    - match
    - player_id
    - match_id
"""

from rest_framework import serializers
from seed.serializers.stats.score import _ScoreSerializer

class ScoreSerializer(_ScoreSerializer):  #
    
    class Meta(_ScoreSerializer.Meta):
        extra_fields = ()
