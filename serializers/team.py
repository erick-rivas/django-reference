from rest_framework import serializers
from models.team import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        depth = 1
