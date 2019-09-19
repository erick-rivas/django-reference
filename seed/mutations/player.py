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
from app.models import File
from seed.schema.types import Player as PlayerType

class SavePlayerMutation(graphene.Mutation):
    
    player = graphene.Field(PlayerType)
    
    class Arguments:
        name = graphene.String(required=True)
        photo = graphene.Int(required=True)
        isActive = graphene.Boolean(required=True)
        team = graphene.Int(required=True)
        type = graphene.Int(required=True)

    def mutate(self, info, **kwargs):

        player = {}
        if "name" in kwargs: player["name"] = kwargs["name"]
        if "isActive" in kwargs: player["is_active"] = kwargs["isActive"]
        if "photo" in kwargs:
             photo = File.objects.get(pk = kwargs["photo"])
             player["photo"] = photo
        if "team" in kwargs:
             team = Team.objects.get(pk = kwargs["team"])
             player["team"] = team
        if "type" in kwargs:
             type = PlayerType.objects.get(pk = kwargs["type"])
             player["type"] = type
        player = Player.objects.create(**player)
        player.save()
    
        return SavePlayerMutation(player=player)

class SetPlayerMutation(graphene.Mutation):
    
    player = graphene.Field(PlayerType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        photo = graphene.Int(required=False)
        isActive = graphene.Boolean(required=False)
        team = graphene.Int(required=False)
        type = graphene.Int(required=False)

    def mutate(self, info, **kwargs):

        player = Player.objects.get(pk=kwargs["id"])
        if "name" in kwargs: player.name = kwargs["name"]
        if "isActive" in kwargs: player.is_active = kwargs["isActive"]
        if "photo" in kwargs:
             photo = File.objects.get(pk = kwargs["photo"])
             player.photo = photo
        if "team" in kwargs:
             team = Team.objects.get(pk = kwargs["team"])
             player.team = team
        if "type" in kwargs:
             type = PlayerType.objects.get(pk = kwargs["type"])
             player.type = type
        player.save()
    
        return SetPlayerMutation(player=player)

class DeletePlayerMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        player = Player.objects.get(pk=kwargs["id"])
        player.delete()
        return DeletePlayerMutation(id=id)