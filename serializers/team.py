"""
__Seed builder__v1.0
  Fields:
    - id
    - name
    - logo_url
    - description
    - market_value
    - players
"""

from rest_framework import serializers
from __seed__.serializers.team import _TeamSerializer

class TeamSerializer(_TeamSerializer):
    class PlayersSerializer(serializers.ModelSerializer):
        pass

    class Meta(_TeamSerializer.Meta):
        pass
