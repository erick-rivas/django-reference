"""
__Seed builder__v1.0

  Base fields:
    - id
    - username
    - first_name
    - last_name
    - email
    - is_active
    - teams
    - team_ids
"""

from rest_framework import serializers
from seed.serializers.user import _UserSerializer

class UserSerializer(_UserSerializer):  #
    
    class Meta(_UserSerializer.Meta):
        extra_fields = ()
