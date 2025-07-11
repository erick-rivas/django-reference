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
from seed.schema.types import resolve_detail
from seed.schema.types import Player as PlayerTypeField

class SavePlayerMutation(graphene.Mutation):
    
    player = graphene.Field(PlayerTypeField)
    
    class Arguments:
        name = graphene.String(required=True)
        photo = graphene.Int(required=True)
        isActive = graphene.Boolean(required=True)
        salary = graphene.Float(required=True)
        team = graphene.Int(required=True)
        position = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        player = {}
        if "name" in kwargs:
            player["name"] = kwargs["name"]
        if "isActive" in kwargs:
            player["is_active"] = kwargs["isActive"]
        if "salary" in kwargs:
            player["salary"] = kwargs["salary"]
        if "photo" in kwargs:
            photo = resolve_detail(File, info, kwargs["photo"])
            player["photo"] = photo
        if "team" in kwargs:
            team = resolve_detail(Team, info, kwargs["team"])
            player["team"] = team
        if "position" in kwargs:
            position = resolve_detail(PlayerPosition, info, kwargs["position"])
            player["position"] = position
        player = \
            Player.objects.create(**player)
        player.save()
    
        return SavePlayerMutation(
            player=player)

class SetPlayerMutation(graphene.Mutation):
    
    player = graphene.Field(PlayerTypeField)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        photo = graphene.Int(required=False)
        isActive = graphene.Boolean(required=False)
        salary = graphene.Float(required=False)
        team = graphene.Int(required=False)
        position = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        player = resolve_detail(Player, info, kwargs["id"])
        if "name" in kwargs:
            player.name = kwargs["name"]
        if "isActive" in kwargs:
            player.is_active = kwargs["isActive"]
        if "salary" in kwargs:
            player.salary = kwargs["salary"]
        if "photo" in kwargs:
            photo = resolve_detail(File, info, kwargs["photo"])
            player.photo = photo
        if "team" in kwargs:
            team = resolve_detail(Team, info, kwargs["team"])
            player.team = team
        if "position" in kwargs:
            position = resolve_detail(PlayerPosition, info, kwargs["position"])
            player.position = position
        player.save()
    
        return SetPlayerMutation(
            player=player)

class DeletePlayerMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        player_id = kwargs["id"]
        player = resolve_detail(Player, info, kwargs["id"])
        player.delete()
        return DeletePlayerMutation(
            id=player_id)