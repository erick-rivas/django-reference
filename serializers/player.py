from rest_framework import serializers
from models.player import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'photo_url', 'team')

    def create(self, validated_data):
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.photo_url = validated_data.get('photo_url', instance.photo_url)
        instance.save()
        return instance