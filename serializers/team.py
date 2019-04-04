from rest_framework import serializers
from serializers.helpers.util import Util
from models.team import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = Util.get_attr_list(Team, 'visitors', 'locals')
        depth = 1
