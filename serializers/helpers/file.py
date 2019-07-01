from rest_framework import serializers
from models.helpers.file import File

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

