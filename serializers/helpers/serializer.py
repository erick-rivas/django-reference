from rest_framework import serializers

class Serializer(serializers.ModelSerializer):  #
    class Meta:
        exclude = ('created_at','updated_at',)
        depth = 0
