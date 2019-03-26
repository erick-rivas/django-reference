from rest_framework import serializers
from models.players import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'photo_url', 'team')
        depth = 1