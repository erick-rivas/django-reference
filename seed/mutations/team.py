"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Team
from app.models import File
from seed.schema.types import resolve_detail
from seed.schema.types import Team as TeamTypeField

class SaveTeamMutation(graphene.Mutation):
    
    team = graphene.Field(TeamTypeField)
    
    class Arguments:
        name = graphene.String(required=True)
        logo = graphene.Int(required=True)
        description = graphene.String(required=True)
        marketValue = graphene.Float(required=True)
        rival = graphene.Int(required=False)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        team = {}
        if "name" in kwargs:
            team["name"] = kwargs["name"]
        if "description" in kwargs:
            team["description"] = kwargs["description"]
        if "marketValue" in kwargs:
            team["market_value"] = kwargs["marketValue"]
        if "logo" in kwargs:
            logo = resolve_detail(File, info, kwargs["logo"])
            team["logo"] = logo
        if "rival" in kwargs:
            rival = resolve_detail(Team, info, kwargs["rival"])
            team["rival"] = rival
        team = \
            Team.objects.create(**team)
        team.save()
    
        return SaveTeamMutation(
            team=team)

class SetTeamMutation(graphene.Mutation):
    
    team = graphene.Field(TeamTypeField)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        logo = graphene.Int(required=False)
        description = graphene.String(required=False)
        marketValue = graphene.Float(required=False)
        rival = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        team = resolve_detail(Team, info, kwargs["id"])
        if "name" in kwargs:
            team.name = kwargs["name"]
        if "description" in kwargs:
            team.description = kwargs["description"]
        if "marketValue" in kwargs:
            team.market_value = kwargs["marketValue"]
        if "logo" in kwargs:
            logo = resolve_detail(File, info, kwargs["logo"])
            team.logo = logo
        if "rival" in kwargs:
            rival = resolve_detail(Team, info, kwargs["rival"])
            team.rival = rival
        team.save()
    
        return SetTeamMutation(
            team=team)

class DeleteTeamMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        team_id = kwargs["id"]
        team = resolve_detail(Team, info, kwargs["id"])
        team.delete()
        return DeleteTeamMutation(
            id=team_id)