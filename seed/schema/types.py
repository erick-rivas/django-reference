"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
import re
from django.db.models import Q
from graphene_django.types import DjangoObjectType
from app.models import Match as MatchModel
from app.models import Player as PlayerModel
from app.models import PlayerType as PlayerTypeModel
from app.models import Score as ScoreModel
from app.models import Team as TeamModel
from app.models import User as UserModel
from app.models import File as FileModel

def query(data, model):
    data = data.replace(".", "__")
    data = data.replace("(", "")
    data = data.replace(")", "")
    res = Q()
    queries = [i.strip() for i in data.split("OR")]
    for q in queries:
        filters = [i.strip() for i in q.split("AND")]
        values = {}
        for f in filters:
            ele = f.split("=")
            values[ele[0].strip()] = ele[1].strip()
        res |= Q(**values)
    return model.objects.filter(res)

class Match(DjangoObjectType):
    class Meta:
        model = MatchModel

class Player(DjangoObjectType):
    class Meta:
        model = PlayerModel

class PlayerType(DjangoObjectType):
    class Meta:
        model = PlayerTypeModel

class Score(DjangoObjectType):
    class Meta:
        model = ScoreModel

class Team(DjangoObjectType):
    class Meta:
        model = TeamModel

class User(DjangoObjectType):
    class Meta:
        model = UserModel
        exclude = ('password',)
class File(DjangoObjectType):
    class Meta:
        model = FileModel

class Query(object):
    
    matches = graphene.List(Match, query=graphene.String())
    match = graphene.Field(Match, id=graphene.Int())
    players = graphene.List(Player, query=graphene.String())
    player = graphene.Field(Player, id=graphene.Int())
    playerTypes = graphene.List(PlayerType, query=graphene.String())
    playerType = graphene.Field(PlayerType, id=graphene.Int())
    scores = graphene.List(Score, query=graphene.String())
    score = graphene.Field(Score, id=graphene.Int())
    teams = graphene.List(Team, query=graphene.String())
    team = graphene.Field(Team, id=graphene.Int())
    users = graphene.List(User, query=graphene.String())
    user = graphene.Field(User, id=graphene.Int())
    files = graphene.List(File, query=graphene.String())
    file = graphene.Field(File, id=graphene.Int())

    def resolve_matches(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], Match)
        return MatchModel.objects.all()
    def resolve_match(self, info, id):
        return MatchModel.objects.get(pk=id)
    
    def resolve_players(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], Player)
        return PlayerModel.objects.all()
    def resolve_player(self, info, id):
        return PlayerModel.objects.get(pk=id)
    
    def resolve_playerTypes(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], PlayerType)
        return PlayerTypeModel.objects.all()
    def resolve_playerType(self, info, id):
        return PlayerTypeModel.objects.get(pk=id)
    
    def resolve_scores(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], Score)
        return ScoreModel.objects.all()
    def resolve_score(self, info, id):
        return ScoreModel.objects.get(pk=id)
    
    def resolve_teams(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], Team)
        return TeamModel.objects.all()
    def resolve_team(self, info, id):
        return TeamModel.objects.get(pk=id)
    
    def resolve_users(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], User)
        return UserModel.objects.all()
    def resolve_user(self, info, id):
        return UserModel.objects.get(pk=id)
    
    def resolve_files(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], File)
        return FileModel.objects.all()
    def resolve_file(self, info, id):
        return FileModel.objects.get(pk=id)