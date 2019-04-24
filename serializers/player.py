from rest_framework import serializers
from serializers.helpers.util import Util
from models.team import Team
from models.player import Player

class PlayerSerializer(serializers.ModelSerializer):
    team_id = serializers.PrimaryKeyRelatedField(source='team', queryset=Team.objects.all(), write_only=True)
    class Meta:
        model = Player
        fields = Util.get_attr_list(Player,
            include=('team_id',))
        depth = 1