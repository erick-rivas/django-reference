"""
__Seed builder__v1.0

  Base fields:
    - id
    - name
"""

from rest_framework import serializers
from seed.serializers.player_position import _PlayerPositionSerializer

class PlayerPositionSerializer(_PlayerPositionSerializer):  #
    
    class Meta(_PlayerPositionSerializer.Meta):
        extra_fields = ()
        fields = _PlayerPositionSerializer.Meta.fields + extra_fields
