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
    - profile_image
    - team_ids
    
  Fields to override (InnerSerializers)
    - teams: Team
"""

from rest_framework import serializers
from serializers.helpers.serializer import InnerSerializer
from _seed.serializers.user import _UserSerializer

class UserSerializer(_UserSerializer):  #
    
    class Meta(_UserSerializer.Meta):
        pass
