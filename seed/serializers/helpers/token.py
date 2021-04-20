"""
__Seed builder__
  (Read_only) Serializer helper
"""

from rest_framework import serializers
from rest_auth.models import TokenModel


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = TokenModel
        fields = (
            'key',
            'user'
        )