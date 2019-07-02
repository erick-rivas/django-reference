"""
__Seed builder__v1.0

  Guidelines: 
    - Modify fields via SeedManifest.yaml (suggested meta: "write & read")
    - Only override serializers fields if required
      - Examples: 
        - Set None to attr to show only pk (attr = None)
        - Set InnerSerializer to attr to show complete model (attr = InnerSerializer(model))
        - For special cases it can inherit from InnerSerializerClass
          - class CustomSerializer(InnerSerializerClass(model))

  Fields:
    - id
    - min
    - player
    - match
    - player_id
    - match_id
    
  Fields to override
    - player: Player
    - match: Match
"""

from rest_framework import serializers
from serializers.helpers.serializer import InnerSerializer
from serializers.helpers.serializer import InnerSerializerClass
from _seed.serializers.score import _ScoreSerializer

class ScoreSerializer(_ScoreSerializer):  #
    
    class Meta(_ScoreSerializer.Meta):
        pass