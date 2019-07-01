"""
__Seed builder__v1.0

  Guidelines: 
    - Modify fields via SeedManifest.yaml (suggested meta: "write & read")
    - Only override serializers if required
      - Example: When it's necessary to increase or limit sent data

  Fields:
    - id
    - name
    - logo
    - description
    - market_value
    - identity_docs
    - players
    - player_ids
    
  Fields to override (InnerSerializers)
    - players: Player
"""

from rest_framework import serializers
from serializers.helpers.serializer import InnerSerializer
from _seed.serializers.team import _TeamSerializer

class TeamSerializer(_TeamSerializer):  #
    
    class Meta(_TeamSerializer.Meta):
        pass
