"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import PlayerType
from seed.schema.types import _PlayerTypeType

class PlayerTypeMutation(graphene.Mutation):
    playerType = graphene.Field(_PlayerTypeType)
    class Arguments:
        id = graphene.Int(required=False)
        name = graphene.String(required=False)

    def mutate(self, info, **kwargs):

        player_type = None
        if "id" in kwargs:
            player_type = PlayerType.objects.get(pk=kwargs["id"])
            if "name" in kwargs: player_type.name = kwargs["name"]
        else:
            player_type = PlayerType.objects.create(
                name = kwargs["name"],
            )
        player_type.save()
    
        return PlayerTypeMutation(playerType=player_type)
