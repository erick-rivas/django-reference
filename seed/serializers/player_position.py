"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""
from seed.helpers.serializer import Serializer
from app.models import PlayerPosition

class _PlayerPositionSerializer(Serializer):  #

    class Meta:
        model = PlayerPosition
        fields = (
            'id',
            'hash',
            'name',  
        )
