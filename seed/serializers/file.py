"""
__Seed builder__
  (Read_only) Serializer helper
"""

from rest_framework import serializers
from seed.models.file import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'id',
            'created_at',
            'hash',
            'url',
            'name',
            'size',
        )
        read_only_fields = (
            'url',
            'name',
            'size'
        )