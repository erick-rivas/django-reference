"""
__Seed builder__v1.0

  Guidelines: 
    - Modify fields via models.json (suggested meta: "write & read")
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
    
  Serializers (to override)
    - LocalSerializer
    - VisitorSerializer
    - ScoresSerializer
"""

from rest_framework import serializers
from __seed__.serializers.match import _MatchSerializer

class MatchSerializer(_MatchSerializer): #
    
    class Meta(_MatchSerializer.Meta):
        pass
