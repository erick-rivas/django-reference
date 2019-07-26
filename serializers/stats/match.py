"""
__Seed builder__v1.0

  Base fields:
    - id
    - date
    - type
    - local
    - visitor
    - scores
    - local_id
    - visitor_id
    - score_ids
"""

from rest_framework import serializers
from seed.serializers.stats.match import _MatchSerializer

class MatchSerializer(_MatchSerializer):  #
    
    class Meta(_MatchSerializer.Meta):
        extra_fields = ()
        fields = _MatchSerializer.Meta.fields + extra_fields
