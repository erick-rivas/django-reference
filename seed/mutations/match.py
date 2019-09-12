"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import Match
from app.models import Team
from app.models import Score
from seed.schema.types import _MatchType

class MatchMutation(graphene.Mutation):
    match = graphene.Field(_MatchType)
    class Arguments:
        id = graphene.Int(required=False)
        date = graphene.DateTime(required=False)
        type = graphene.String(required=False)
        localId = graphene.Int(required=False)
        visitorId = graphene.Int(required=False)

    def mutate(self, info, **kwargs):

        match = None
        if "id" in kwargs:
            match = Match.objects.get(pk=kwargs["id"])
            if "date" in kwargs: match.date = kwargs["date"]
            if "type" in kwargs: match.type = kwargs["type"]
            if "localId" in kwargs: 
                local = Team.objects.get(pk = kwargs["localId"])
                match.local = local
            if "visitorId" in kwargs: 
                visitor = Team.objects.get(pk = kwargs["visitorId"])
                match.visitor = visitor
        else:
            local = Team.objects.get(pk = kwargs["localId"])
            visitor = Team.objects.get(pk = kwargs["visitorId"])
            match = Match.objects.create(
                date = kwargs["date"],
                type = kwargs["type"],
                local = local,
                visitor = visitor,
            )
        match.save()
    
        return MatchMutation(match=match)
