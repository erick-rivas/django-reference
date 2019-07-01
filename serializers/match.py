"""
__Seed builder__v1.0

  Guidelines: 
    - Modify fields via SeedManifest.yaml (suggested meta: "write & read")
    - Only override serializers if required
      - Example: When it's necessary to increase or limit sent data

  Fields:
    - id
    - date
    - type
    - local
    - visitor
    - scores
    - local_id
    - visitor_id
    - score_ids
    
  Fields to override (InnerSerializers)
    - local: Team
    - visitor: Team
    - scores: Score
"""

from rest_framework import serializers
from serializers.helpers.serializer import InnerSerializer
from _seed.serializers.match import _MatchSerializer

class MatchSerializer(_MatchSerializer):  #
    
    class Meta(_MatchSerializer.Meta):
        pass
