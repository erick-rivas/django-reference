"""
__Seed builder__v1.0

  Guidelines: 
    - Modify fields via SeedManifest.yaml (suggested meta: "write & read")
    - Only override serializers fields if required
    - Override rules: 
      - Set None to attr to show only pk (attr = None)
      - Set InnerSerializer to attr to show complete model (attr = InnerSerializer(model))
      - For special cases, inherit from InnerSerializerClass
        - class CustomSerializer(InnerSerializerClass(model))
    - Reference: https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

  Fields:
    - id
    - name
    - photo
    - is_active
    - team
    - team_id
    
  Override fields
    - team: Team
"""

from rest_framework import serializers
from serializers.helpers.serializer import InnerSerializer
from serializers.helpers.serializer import InnerSerializerClass
from _seed.serializers.player import _PlayerSerializer

class PlayerSerializer(_PlayerSerializer):  #
    
    class Meta(_PlayerSerializer.Meta):
        pass

