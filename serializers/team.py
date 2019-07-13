"""
__Seed builder__v1.0

  Guidelines: 
    - Only add aggregate methods or definitions if required
    - Reference: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

  Base fields:
    - id
    - name
    - logo
    - description
    - market_value
    - rival
    - identity_docs
    - players
    - rival_id
    - player_ids
"""

from rest_framework import serializers
from seed.serializers.team import _TeamSerializer

class TeamSerializer(_TeamSerializer):  #
    
    class Meta(_TeamSerializer.Meta):
        extra_fields = ()
