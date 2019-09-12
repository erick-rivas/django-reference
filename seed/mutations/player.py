"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import Player
from app.models import Team
from app.models import PlayerType
from seed.schema.types import _PlayerType

class PlayerMutation(graphene.Mutation):
    player = graphene.Field(_PlayerType)
    class Arguments:
        id = graphene.Int(required=False)
        name = graphene.String(required=False)
        photoId = graphene.Int(required=False)
        isActive = graphene.Boolean(required=False)
        teamId = graphene.Int(required=False)
        typeId = graphene.Int(required=False)

    def mutate(self, info, **kwargs):

        player = None
        if "id" in kwargs:
            player = Player.objects.get(pk=kwargs["id"])
            if "name" in kwargs: player.name = kwargs["name"]
            if "isActive" in kwargs: player.is_active = kwargs["isActive"]
            if "photoId" in kwargs: 
                photo = Image.objects.get(pk = kwargs["photoId"])
                player.photo = photo
            if "teamId" in kwargs: 
                team = Team.objects.get(pk = kwargs["teamId"])
                player.team = team
            if "typeId" in kwargs: 
                type = PlayerType.objects.get(pk = kwargs["typeId"])
                player.type = type
        else:
            photo = Image.objects.get(pk = kwargs["photoId"])
            team = Team.objects.get(pk = kwargs["teamId"])
            type = PlayerType.objects.get(pk = kwargs["typeId"])
            player = Player.objects.create(
                name = kwargs["name"],
                is_active = kwargs["isActive"],
                photo = photo,
                team = team,
                type = type,
            )
        player.save()
    
        return PlayerMutation(player=player)
