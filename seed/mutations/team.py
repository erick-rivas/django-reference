"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import Team
from app.models import Player
from seed.schema.types import _TeamType

class TeamMutation(graphene.Mutation):
    team = graphene.Field(_TeamType)
    class Arguments:
        id = graphene.Int(required=False)
        name = graphene.String(required=False)
        logoId = graphene.Int(required=False)
        description = graphene.String(required=False)
        marketValue = graphene.Float(required=False)
        rivalId = graphene.Int(required=False)

    def mutate(self, info, **kwargs):

        team = None
        if "id" in kwargs:
            team = Team.objects.get(pk=kwargs["id"])
            if "name" in kwargs: team.name = kwargs["name"]
            if "description" in kwargs: team.description = kwargs["description"]
            if "marketValue" in kwargs: team.market_value = kwargs["marketValue"]
            if "logoId" in kwargs: 
                logo = Image.objects.get(pk = kwargs["logoId"])
                team.logo = logo
            if "rivalId" in kwargs: 
                rival = Team.objects.get(pk = kwargs["rivalId"])
                team.rival = rival
        else:
            logo = Image.objects.get(pk = kwargs["logoId"])
            rival = Team.objects.get(pk = kwargs["rivalId"])
            team = Team.objects.create(
                name = kwargs["name"],
                description = kwargs["description"],
                market_value = kwargs["marketValue"],
                logo = logo,
                rival = rival,
            )
        team.save()
    
        return TeamMutation(team=team)
