"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import User
from app.models import Team
from app.models import File
from seed.schema.types import resolve_detail
from seed.schema.types import User as UserTypeField

class SaveUserMutation(graphene.Mutation):
    
    user = graphene.Field(UserTypeField)
    
    class Arguments:
        username = graphene.String(required=True)
        firstName = graphene.String(required=True)
        lastName = graphene.String(required=True)
        email = graphene.String(required=True)
        isActive = graphene.Boolean(required=True)
        password = graphene.String(required=True)
        profileImage = graphene.Int(required=True)
        teams = graphene.List(graphene.Int)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        user = {}
        if "userName" in kwargs:
            user["user_name"] = kwargs["userName"]
        if "firstName" in kwargs:
            user["first_name"] = kwargs["firstName"]
        if "lastName" in kwargs:
            user["last_name"] = kwargs["lastName"]
        if "email" in kwargs:
            user["email"] = kwargs["email"]
        if "isActive" in kwargs:
            user["is_active"] = kwargs["isActive"]
        if "profileImage" in kwargs:
            profile_image = resolve_detail(File, info, kwargs["profileImage"])
            user["profile_image"] = profile_image
        user = \
            User.objects.create(**user)
        if "password" in kwargs: user.set_password(kwargs["password"])
        if "teams" in kwargs:
            user.teams.clear()
            for teams_id in kwargs["teams"]:
                teams = resolve_detail(Team, info, teams_id)
                user.teams.add(teams)
        user.save()
    
        return SaveUserMutation(
            user=user)

class SetUserMutation(graphene.Mutation):
    
    user = graphene.Field(UserTypeField)
    
    class Arguments:
        id = graphene.Int(required=True)
        username = graphene.String(required=False)
        firstName = graphene.String(required=False)
        lastName = graphene.String(required=False)
        email = graphene.String(required=False)
        isActive = graphene.Boolean(required=False)
        password = graphene.String(required=False)
        profileImage = graphene.Int(required=False)
        teams = graphene.List(graphene.Int)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        user = resolve_detail(User, info, kwargs["id"])
        if "userName" in kwargs:
            user.user_name = kwargs["userName"]
        if "firstName" in kwargs:
            user.first_name = kwargs["firstName"]
        if "lastName" in kwargs:
            user.last_name = kwargs["lastName"]
        if "email" in kwargs:
            user.email = kwargs["email"]
        if "isActive" in kwargs:
            user.is_active = kwargs["isActive"]
        if "password" in kwargs:
            user.set_password(kwargs["password"])
        if "profileImage" in kwargs:
            profile_image = resolve_detail(File, info, kwargs["profileImage"])
            user.profile_image = profile_image
        if "teams" in kwargs:
            user.teams.clear()
            for teams_id in kwargs["teams"]:
                teams = resolve_detail(Team, info, teams_id)
                user.teams.add(teams)
        user.save()
    
        return SetUserMutation(
            user=user)

class DeleteUserMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        user_id = kwargs["id"]
        user = resolve_detail(User, info, kwargs["id"])
        user.delete()
        return DeleteUserMutation(
            id=user_id)