"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import User
from app.models import Team
from seed.schema.types import _UserType

class UserMutation(graphene.Mutation):
    user = graphene.Field(_UserType)
    class Arguments:
        id = graphene.Int(required=False)
        username = graphene.String(required=False)
        firstName = graphene.String(required=False)
        lastName = graphene.String(required=False)
        email = graphene.String(required=False)
        is_active = graphene.Boolean(required=False)
        password = graphene.String(required=False)
        teamIds = graphene.List(graphene.Int)

    def mutate(self, info, **kwargs):

        user = None
        if "id" in kwargs:
            user = User.objects.get(pk=kwargs["id"])
            if "userName" in kwargs: user.user_name = kwargs["userName"]
            if "firstName" in kwargs: user.first_name = kwargs["firstName"]
            if "lastName" in kwargs: user.last_name = kwargs["lastName"]
            if "email" in kwargs: user.email = kwargs["email"]
            if "is_active" in kwargs: user.is_active = kwargs["is_active"]
            if "password" in kwargs: user.setPassword(kwargs["password"])
        else:
            user = User.objects.create(
                user_name = kwargs["userName"],
                first_name = kwargs["firstName"],
                last_name = kwargs["lastName"],
                email = kwargs["email"],
                is_active = kwargs["is_active"],
            )
        user.setPassword(kwargs["password"])
        if "teamIds" in kwargs:
            user.team = [] 
            for id in kwargs["teamIds"]:
                teams = Team.objects.get(pk = id)
                user.teams.add(teams)
        user.save()
    
        return UserMutation(user=user)
