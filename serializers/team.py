"""
__Seed builder__v1.0

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
        fields = _TeamSerializer.Meta.fields + extra_fields
