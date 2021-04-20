"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Team
from app.models import File
from seed.schema.types import Team as TeamType

class SaveTeamMutation(graphene.Mutation):
    
    team = graphene.Field(TeamType)
    
    class Arguments:
        name = graphene.String(required=True)
        logo = graphene.Int(required=True)
        description = graphene.String(required=True)
        marketValue = graphene.Float(required=True)
        rival = graphene.Int(required=False)

    def mutate(self, info, **kwargs):
        user = info.context.user
        team = {}
        if "name" in kwargs: team["name"] = kwargs["name"]
        if "description" in kwargs: team["description"] = kwargs["description"]
        if "marketValue" in kwargs: team["market_value"] = kwargs["marketValue"]
        if "logo" in kwargs:
            logo = File.filter_permissions(
                File.objects, File.permission_filters(user))\
                .get(pk=kwargs["logo"])
            team["logo"] = logo
        if "rival" in kwargs:
            rival = Team.filter_permissions(
                Team.objects, Team.permission_filters(user))\
                .get(pk=kwargs["rival"])
            team["rival"] = rival
        team = Team.objects.create(**team)
        team.save()
    
        return SaveTeamMutation(team=team)

class SetTeamMutation(graphene.Mutation):
    
    team = graphene.Field(TeamType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        logo = graphene.Int(required=False)
        description = graphene.String(required=False)
        marketValue = graphene.Float(required=False)
        rival = graphene.Int(required=False)

    def mutate(self, info, **kwargs):
        user = info.context.user
        team = Team.filter_permissions(
            Team.objects, Team.permission_filters(user))\
            .get(pk=kwargs["id"])
        if "name" in kwargs: team.name = kwargs["name"]
        if "description" in kwargs: team.description = kwargs["description"]
        if "marketValue" in kwargs: team.market_value = kwargs["marketValue"]
        if "logo" in kwargs:
            logo = File.objects.get(pk=kwargs["logo"])
            team.logo = logo
        if "rival" in kwargs:
            rival = Team.objects.get(pk=kwargs["rival"])
            team.rival = rival
        team.save()
    
        return SetTeamMutation(team=team)

class DeleteTeamMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        team_id = kwargs["id"]
        team = Team.objects.get(pk=kwargs["id"])
        team.delete()
        return DeleteTeamMutation(id=team_id)