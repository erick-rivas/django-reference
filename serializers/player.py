"""
__Seed builder__v1.0

  Base fields:
    - id
    - name
    - photo
    - is_active
    - team
    - position
    - team_id
    - position_id
"""

from rest_framework import serializers
from seed.serializers.player import _PlayerSerializer

class PlayerSerializer(_PlayerSerializer):  #
    
    class Meta(_PlayerSerializer.Meta):
        extra_fields = ()
        fields = _PlayerSerializer.Meta.fields + extra_fields
