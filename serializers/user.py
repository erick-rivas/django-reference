"""
__Seed builder__v1.0
  Fields:
    - id
    - username
    - first_name
    - last_name
    - email
    - is_active
    - teams
"""

from rest_framework import serializers
from __seed__.serializers.user import _UserSerializer

class UserSerializer(_UserSerializer):
    class TeamsSerializer(serializers.ModelSerializer):
        pass

    class Meta(_UserSerializer.Meta):
        pass
