"""
__Seed builder__v1.0

  Base fields:
    - id
    - name
"""

from rest_framework import serializers
from seed.serializers.player_type import _PlayerTypeSerializer

class PlayerTypeSerializer(_PlayerTypeSerializer):  #
    
    class Meta(_PlayerTypeSerializer.Meta):
        extra_fields = ()
        fields = _PlayerTypeSerializer.Meta.fields + extra_fields
