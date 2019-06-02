"""
__Seed builder__v1.0

  Guidelines: 
    - Modify fields via models.json (suggested meta: "write & read")
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
    
  Serializers (to override)
    - TeamsSerializer
"""

from rest_framework import serializers
from __seed__.serializers.user import _UserSerializer

class UserSerializer(_UserSerializer): #
    
    class Meta(_UserSerializer.Meta):
        pass
