"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import PlayerPosition

class _PlayerPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerPosition
        fields = (
            'id',
            'hash',
            'name',  
        )