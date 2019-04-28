from rest_framework import serializers
from models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'image_url', 'color')
        depth = 1
