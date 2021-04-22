"""
__Seed builder__
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
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        player = {}
        if "name" in kwargs: player["name"] = kwargs["name"]
        if "isActive" in kwargs: player["is_active"] = kwargs["isActive"]
        if "photo" in kwargs:
            photo = File.filter_permissions(
                File.objects, File.permission_filters(user))\
                .get(pk=kwargs["photo"])
            player["photo"] = photo
        if "team" in kwargs:
            team = Team.filter_permissions(
                Team.objects, Team.permission_filters(user))\
                .get(pk=kwargs["team"])
            player["team"] = team
        if "position" in kwargs:
            position = PlayerPosition.filter_permissions(
                PlayerPosition.objects, PlayerPosition.permission_filters(user))\
                .get(pk=kwargs["position"])
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
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        player = Player.filter_permissions(
            Player.objects, Player.permission_filters(user))\
            .get(pk=kwargs["id"])
        if "name" in kwargs: player.name = kwargs["name"]
        if "isActive" in kwargs: player.is_active = kwargs["isActive"]
        if "photo" in kwargs:
            photo = File.objects.get(pk=kwargs["photo"])
            player.photo = photo
        if "team" in kwargs:
            team = Team.objects.get(pk=kwargs["team"])
            player.team = team
        if "position" in kwargs:
            position = PlayerPosition.objects.get(pk=kwargs["position"])
            player.position = position
        player.save()
    
        return SetPlayerMutation(player=player)

class DeletePlayerMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        player_id = kwargs["id"]
        player = Player.objects.get(pk=kwargs["id"])
        player.delete()
        return DeletePlayerMutation(id=player_id)