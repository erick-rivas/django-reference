"""
__Seed builder__v1.0

  Guidelines: 
    - Only add aggregate methods or definitions if required
    - Reference: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

  Base fields:
    - id
    - name
    - photo
    - is_active
    - team
    - team_id
"""

from rest_framework import serializers
from seed.serializers.player import _PlayerSerializer

class PlayerSerializer(_PlayerSerializer):  #
    
    class Meta(_PlayerSerializer.Meta):
        extra_fields = ()
