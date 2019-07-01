"""
__Seed builder__v1.0

  Guidelines: 
    - Modify fields via SeedManifest.yaml (suggested meta: "write & read")
    - Only override serializers if required
      - Example: When it's necessary to increase or limit sent data

  Fields:
    - id
    - min
    - player
    - match
    - player_id
    - match_id
    
  Fields to override (InnerSerializers)
    - player: Player
    - match: Match
"""

from rest_framework import serializers
from serializers.helpers.serializer import InnerSerializer
from _seed.serializers.score import _ScoreSerializer

class ScoreSerializer(_ScoreSerializer):  #
    
    class Meta(_ScoreSerializer.Meta):
        pass