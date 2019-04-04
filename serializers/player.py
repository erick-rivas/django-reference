from rest_framework import serializers
from serializers.helpers.util import Util
from models.player import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = Util.get_attr_list(Player)
        depth = 1
