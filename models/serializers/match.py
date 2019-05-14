from rest_framework import serializers
from models.serializers.helpers.util import Util
from models.match import Match
from models.team import Team

class MatchSerializer(serializers.ModelSerializer):
    visitor_id = serializers.PrimaryKeyRelatedField(source='visitor', queryset=Team.objects.all(), write_only=True)
    local_id = serializers.PrimaryKeyRelatedField(source='local', queryset=Team.objects.all(), write_only=True)
    class Meta:
        model = Match
        fields = Util.get_attr_list(Match,
            include=('visitor_id', 'local_id'))
        depth = 1