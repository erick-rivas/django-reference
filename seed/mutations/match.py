"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Match
from app.models import Team
from seed.schema.types import resolve_detail
from seed.schema.types import Match as MatchTypeField

class SaveMatchMutation(graphene.Mutation):
    
    match = graphene.Field(MatchTypeField)
    
    class Arguments:
        date = graphene.DateTime(required=True)
        type = graphene.String(required=True)
        local = graphene.Int(required=True)
        visitor = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        match = {}
        if "date" in kwargs:
            match["date"] = kwargs["date"]
        if "type" in kwargs:
            match["type"] = kwargs["type"]
        if "local" in kwargs:
            local = resolve_detail(Team, info, kwargs["local"])
            match["local"] = local
        if "visitor" in kwargs:
            visitor = resolve_detail(Team, info, kwargs["visitor"])
            match["visitor"] = visitor
        match = \
            Match.objects.create(**match)
        match.save()
    
        return SaveMatchMutation(
            match=match)

class SetMatchMutation(graphene.Mutation):
    
    match = graphene.Field(MatchTypeField)
    
    class Arguments:
        id = graphene.Int(required=True)
        date = graphene.DateTime(required=False)
        type = graphene.String(required=False)
        local = graphene.Int(required=False)
        visitor = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        match = resolve_detail(Match, info, kwargs["id"])
        if "date" in kwargs:
            match.date = kwargs["date"]
        if "type" in kwargs:
            match.type = kwargs["type"]
        if "local" in kwargs:
            local = resolve_detail(Team, info, kwargs["local"])
            match.local = local
        if "visitor" in kwargs:
            visitor = resolve_detail(Team, info, kwargs["visitor"])
            match.visitor = visitor
        match.save()
    
        return SetMatchMutation(
            match=match)

class DeleteMatchMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        match_id = kwargs["id"]
        match = resolve_detail(Match, info, kwargs["id"])
        match.delete()
        return DeleteMatchMutation(
            id=match_id)