"""
__Seed builder__v1.0
  Fields:
    - id
    - name
    - photo_url
    - is_active
    - team
    - team_id
"""

from rest_framework import serializers
from __seed__.serializers.player import _PlayerSerializer

class PlayerSerializer(_PlayerSerializer):
    class TeamSerializer(serializers.ModelSerializer):
        pass

    class Meta(_PlayerSerializer.Meta):
        pass
