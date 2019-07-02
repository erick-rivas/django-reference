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
    - date
    - type
    - local
    - visitor
    - scores
    - local_id
    - visitor_id
    - score_ids
    
  Fields to override
    - local: Team
    - visitor: Team
    - scores: Score
"""

from rest_framework import serializers
from serializers.helpers.serializer import InnerSerializer
from serializers.helpers.serializer import InnerSerializerClass
from _seed.serializers.match import _MatchSerializer

class MatchSerializer(_MatchSerializer):  #
    
    class Meta(_MatchSerializer.Meta):
        pass
