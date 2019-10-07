"""
__Seed builder__v0.1.7
  (Read_only) Builder helper
"""

from rest_framework import serializers
from rest_auth.models import TokenModel

class TokenSerializer(serializers.ModelSerializer):  #

    class Meta:
        model = TokenModel
        fields = (
            'key',
            'user'
        )
