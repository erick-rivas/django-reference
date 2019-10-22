"""
__Seed builder__v0.1.8
  (Read_only) Builder helper
"""

from rest_framework import serializers
from seed.models.helpers.file import File

class FileSerializer(serializers.ModelSerializer):  #

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

