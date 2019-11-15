"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import PlayerPosition
from app.models import File
from seed.schema.types import PlayerPosition as PlayerPositionType

class SavePlayerPositionMutation(graphene.Mutation):
    
    playerPosition = graphene.Field(PlayerPositionType)
    
    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, **kwargs):

        player_position = {}
        if "name" in kwargs: player_position["name"] = kwargs["name"]
        player_position = PlayerPosition.objects.create(**player_position)
        player_position.save()
    
        return SavePlayerPositionMutation(playerPosition=player_position)

class SetPlayerPositionMutation(graphene.Mutation):
    
    playerPosition = graphene.Field(PlayerPositionType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)

    def mutate(self, info, **kwargs):

        player_position = PlayerPosition.objects.get(pk=kwargs["id"])
        if "name" in kwargs: player_position.name = kwargs["name"]
        player_position.save()
    
        return SetPlayerPositionMutation(playerPosition=player_position)

class DeletePlayerPositionMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        player_position = PlayerPosition.objects.get(pk=kwargs["id"])
        player_position.delete()
        return DeletePlayerPositionMutation(id=id)
