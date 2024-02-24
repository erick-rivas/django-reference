"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import PlayerPosition
from graphene.types.generic import GenericScalar
from seed.schema.types import PlayerPosition as PlayerPositionTypeField

class SavePlayerPositionMutation(graphene.Mutation):
    
    playerPosition = graphene.Field(PlayerPositionTypeField)
    
    class Arguments:
        name = graphene.String(required=True)
        code = graphene.String(required=True)
        stats = GenericScalar(required=True)
        details = GenericScalar(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        player_position = {}
        if "name" in kwargs:
            player_position["name"] = kwargs["name"]
        if "code" in kwargs:
            player_position["code"] = kwargs["code"]
        if "stats" in kwargs:
            player_position["stats"] = kwargs["stats"]
        if "details" in kwargs:
            player_position["details"] = kwargs["details"]
        player_position = \
            PlayerPosition.objects.create(**player_position)
        player_position.save()
    
        return SavePlayerPositionMutation(
            playerPosition=player_position)

class SetPlayerPositionMutation(graphene.Mutation):
    
    playerPosition = graphene.Field(PlayerPositionTypeField)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        code = graphene.String(required=False)
        stats = GenericScalar(required=False)
        details = GenericScalar(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        player_position = PlayerPosition.filter_permissions(
            PlayerPosition.objects,
            PlayerPosition.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "name" in kwargs:
            player_position.name = kwargs["name"]
        if "code" in kwargs:
            player_position.code = kwargs["code"]
        if "stats" in kwargs:
            player_position.stats = kwargs["stats"]
        if "details" in kwargs:
            player_position.details = kwargs["details"]
        player_position.save()
    
        return SetPlayerPositionMutation(
            playerPosition=player_position)

class DeletePlayerPositionMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        player_position_id = kwargs["id"]
        player_position = PlayerPosition.objects.get(pk=kwargs["id"])
        player_position.delete()
        return DeletePlayerPositionMutation(
            id=player_position_id)