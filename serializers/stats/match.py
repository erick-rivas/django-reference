"""
__Seed builder__v1.0

  Guidelines: 
    - Only add aggregate methods or definitions if required
    - Reference: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

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
