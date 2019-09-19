"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import PlayerType
from app.models import File
from seed.schema.types import PlayerType as PlayerTypeType

class SavePlayerTypeMutation(graphene.Mutation):
    
    playerType = graphene.Field(PlayerTypeType)
    
    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, **kwargs):

        player_type = {}
        if "name" in kwargs: player_type["name"] = kwargs["name"]
        player_type = PlayerType.objects.create(**player_type)
        player_type.save()
    
        return SavePlayerTypeMutation(playerType=player_type)

class SetPlayerTypeMutation(graphene.Mutation):
    
    playerType = graphene.Field(PlayerTypeType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)

    def mutate(self, info, **kwargs):

        player_type = PlayerType.objects.get(pk=kwargs["id"])
        if "name" in kwargs: player_type.name = kwargs["name"]
        player_type.save()
    
        return SetPlayerTypeMutation(playerType=player_type)

class DeletePlayerTypeMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        player_type = PlayerType.objects.get(pk=kwargs["id"])
        player_type.delete()
        return DeletePlayerTypeMutation(id=id)
