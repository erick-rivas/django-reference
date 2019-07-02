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
    - name
    - logo
    - description
    - market_value
    - identity_docs
    - players
    - player_ids
    
  Fields to override
    - players: Player
"""

from rest_framework import serializers
from serializers.helpers.serializer import InnerSerializer
from serializers.helpers.serializer import InnerSerializerClass
from _seed.serializers.team import _TeamSerializer

class TeamSerializer(_TeamSerializer):  #
    
    class Meta(_TeamSerializer.Meta):
        pass
