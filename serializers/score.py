"""
__Seed builder__v1.0

  Guidelines: 
    - Modify fields via models.json (suggested meta: "write & read")
    - Only override serializers if required
      - Example: When it's necessary to increase or limit sent data

  Fields:
    - id
    - min
    - player
    - match
    - player_id
    - match_id
    
  Serializers (to override)
    - PlayerSerializer
    - MatchSerializer
"""

from rest_framework import serializers
from __seed__.serializers.score import _ScoreSerializer

class ScoreSerializer(_ScoreSerializer): #
    
    class Meta(_ScoreSerializer.Meta):
        pass