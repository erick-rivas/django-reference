from rest_framework import serializers
from models.serializers.helpers.util import Util
from models.team import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = Util.get_attr_list(Team,
            exclude=('visitors', 'locals'))
        depth = 1
