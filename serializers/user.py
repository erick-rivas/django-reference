"""
__Seed builder__v1.0

  Guidelines: 
    - Only add aggregate methods or definitions if required
    - Reference: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

  Base fields:
    - id
    - username
    - first_name
    - last_name
    - email
    - is_active
    - teams
    - team_ids
"""

from rest_framework import serializers
from seed.serializers.user import _UserSerializer

class UserSerializer(_UserSerializer):  #
    
    class Meta(_UserSerializer.Meta):
        extra_fields = ()
