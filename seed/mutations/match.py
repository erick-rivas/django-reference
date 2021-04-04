"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Match
from app.models import Team
from seed.schema.types import Match as MatchType

class SaveMatchMutation(graphene.Mutation):
    
    match = graphene.Field(MatchType)
    
    class Arguments:
        date = graphene.DateTime(required=True)
        type = graphene.String(required=True)
        local = graphene.Int(required=True)
        visitor = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        user = info.context.user
        match = {}
        if "date" in kwargs: match["date"] = kwargs["date"]
        if "type" in kwargs: match["type"] = kwargs["type"]
        if "local" in kwargs:
             local = Team.filter_permissions(Team.objects, Team.permission_filters(user)).get(pk = kwargs["local"])
             match["local"] = local
        if "visitor" in kwargs:
             visitor = Team.filter_permissions(Team.objects, Team.permission_filters(user)).get(pk = kwargs["visitor"])
             match["visitor"] = visitor
        match = Match.objects.create(**match)
        match.save()
    
        return SaveMatchMutation(match=match)

class SetMatchMutation(graphene.Mutation):
    
    match = graphene.Field(MatchType)
    
    class Arguments:
        id = graphene.Int(required=True)
        date = graphene.DateTime(required=False)
        type = graphene.String(required=False)
        local = graphene.Int(required=False)
        visitor = graphene.Int(required=False)

    def mutate(self, info, **kwargs):
        user = info.context.user
        match = Match.filter_permissions(Match.objects, Match.permission_filters(user)).get(pk=kwargs["id"])
        if "date" in kwargs: match.date = kwargs["date"]
        if "type" in kwargs: match.type = kwargs["type"]
        if "local" in kwargs:
             local = Team.objects.get(pk = kwargs["local"])
             match.local = local
        if "visitor" in kwargs:
             visitor = Team.objects.get(pk = kwargs["visitor"])
             match.visitor = visitor
        match.save()
    
        return SetMatchMutation(match=match)

class DeleteMatchMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        match_id = kwargs["id"]
        match = Match.objects.get(pk=kwargs["id"])
        match.delete()
        return DeleteMatchMutation(id=match_id)