from rest_framework import serializers
from serializers.helpers.util import Util
from models.score import Score

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = Util.get_attr_list(Score)
        depth = 1
