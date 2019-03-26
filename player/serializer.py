from rest_framework import serializers
from player.models import Player

class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'photo_url')
