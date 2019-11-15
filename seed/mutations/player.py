"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Player
from app.models import Team
from app.models import PlayerPosition
from app.models import File
from seed.schema.types import Player as PlayerType

class SavePlayerMutation(graphene.Mutation):
    
    player = graphene.Field(PlayerType)
    
    class Arguments:
        name = graphene.String(required=True)
        photo = graphene.Int(required=True)
        isActive = graphene.Boolean(required=True)
        team = graphene.Int(required=True)
        position = graphene.Int(required=True)

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
        if "position" in kwargs:
             position = PlayerPosition.objects.get(pk = kwargs["position"])
             player["position"] = position
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
        position = graphene.Int(required=False)

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
        if "position" in kwargs:
             position = PlayerPosition.objects.get(pk = kwargs["position"])
             player.position = position
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
