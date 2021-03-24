"""
__Seed builder__v0.2.0
  (Read_only) Builder helper
"""

from rest_framework import serializers
from seed.models.file import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'id',
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