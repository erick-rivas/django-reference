"""
__Seed builder__v1.0

  Guidelines: 
    - Only add aggregate methods or definitions if required
    - Reference: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

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
