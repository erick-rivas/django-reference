"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import PlayerPosition

class PlayerPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerPosition
        fields = (
            'id',
            'hash',
            'name',  
        )