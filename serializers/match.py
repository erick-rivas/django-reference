from rest_framework import serializers
from serializers.helpers.util import Util
from models.match import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = Util.get_attr_list(Match)
        depth = 1
