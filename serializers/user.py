"""
__Seed builder__v1.0

  Guidelines: 
    - Modify fields via SeedManifest.yaml (suggested meta: "write & read")
    - Only override serializers if required
      - Example: When it's necessary to increase or limit sent data

  Fields:
    - id
    - username
    - first_name
    - last_name
    - email
    - is_active
    - teams
    - team_ids
    
  Serializers (to override)
    - TeamsSerializer
"""

from rest_framework import serializers
from _seed.serializers.user import _UserSerializer

class UserSerializer(_UserSerializer): #
    
    class Meta(_UserSerializer.Meta):
        pass
