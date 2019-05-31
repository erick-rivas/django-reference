"""
__Seed builder__v1.0
  Fields:
    - id
    - date
    - type
    - local
    - visitor
    - scores
    - local_id
    - visitor_id
"""

from rest_framework import serializers
from __seed__.serializers.match import _MatchSerializer

class MatchSerializer(_MatchSerializer):
    class LocalSerializer(serializers.ModelSerializer):
        pass
    class VisitorSerializer(serializers.ModelSerializer):
        pass
    class ScoresSerializer(serializers.ModelSerializer):
        pass

    class Meta(_MatchSerializer.Meta):
        pass
