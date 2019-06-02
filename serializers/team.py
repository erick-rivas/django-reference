"""
__Seed builder__v1.0

  Guidelines: 
    - Modify fields via models.json (suggested meta: "write & read")
    - Only override serializers if required
      - Example: When it's necessary to increase or limit sent data

  Fields:
    - id
    - name
    - logo_url
    - description
    - market_value
    - players
    
  Serializers (to override)
    - PlayersSerializer
"""

from rest_framework import serializers
from __seed__.serializers.team import _TeamSerializer

class TeamSerializer(_TeamSerializer): #
    
    class Meta(_TeamSerializer.Meta):
        pass
