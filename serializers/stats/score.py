"""
__Seed builder__v1.0

  Guidelines: 
    - Modify fields via SeedManifest.yaml (suggested meta: "write & read")
    - Only override serializers fields if required
    - Override rules: 
      - Set None to attr to show only pk (attr = None)
      - Set InnerSerializer to attr to show complete model (attr = InnerSerializer(model))
      - For special cases, inherit from InnerSerializerClass
        - class CustomSerializer(InnerSerializerClass(model))
    - Reference: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

  Fields:
    - id
    - min
    - player
    - match
    - player_id
    - match_id
    
  Override fields
    - player: Player
    - match: Match
"""

from rest_framework import serializers
from seed.serializers.stats.score import _ScoreSerializer

class ScoreSerializer(_ScoreSerializer):  #
    
    class Meta(_ScoreSerializer.Meta):
        pass