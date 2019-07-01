"""
__Seed builder__v1.0

  Guidelines: 
    - Modify fields via SeedManifest.yaml (suggested meta: "write & read")
    - Only override serializers if required
      - Example: When it's necessary to increase or limit sent data

  Fields:
    - id
    - name
    - photo
    - is_active
    - team
    - team_id
    
  Fields to override (InnerSerializers)
    - team: Team
"""

from rest_framework import serializers
from serializers.helpers.serializer import InnerSerializer
from _seed.serializers.player import _PlayerSerializer

class PlayerSerializer(_PlayerSerializer):  #
    
    class Meta(_PlayerSerializer.Meta):
        pass
