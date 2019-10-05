"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import re
import graphene
from django.db.models import Q
from graphene_django.types import DjangoObjectType
from app.models import Match as MatchModel
from app.models import Player as PlayerModel
from app.models import PlayerPosition as PlayerPositionModel
from app.models import Score as ScoreModel
from app.models import Team as TeamModel
from app.models import User as UserModel
from app.models import File as FileModel

def query(data, model):
    def snake_case(name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    data = data.replace(".", "__")
    data = data.replace("(", "")
    data = data.replace(")", "")
    res = Q()
    queries = [i.strip() for i in data.split("OR")]
    for q in queries:
        filters = [i.strip() for i in q.split("AND")]
        values = {}
        for f in filters:
            opt = ("=", "")
            if ">=" in f: opt = (">=", "gte")
            elif "<=" in f: opt = ("<=", "lte")
            elif ">" in f: opt = (">", "gt")
            elif "<" in f: opt = ("<", "lt")
            ele = f.split(opt[0])
            if opt[0] == "==":
              values[snake_case(ele[0].strip())] = ele[1].strip()
            else:
                values[snake_case(ele[0].strip()) + "__" + opt[1]] = ele[1].strip()
        res |= Q(**values)
    return model.objects.filter(res)

class Match(DjangoObjectType):
    class Meta:
        model = MatchModel
        description = "Represents a match between two teams  (A vs B)"

class Player(DjangoObjectType):
    class Meta:
        model = PlayerModel

class PlayerPosition(DjangoObjectType):
    class Meta:
        model = PlayerPositionModel
        description = "Represents a player  position (eg. forward)"

class Score(DjangoObjectType):
    class Meta:
        model = ScoreModel
        description = "Represents a match score (goal)"

class Team(DjangoObjectType):
    class Meta:
        model = TeamModel

class User(DjangoObjectType):
    class Meta:
        model = UserModel
        exclude = ('password',)
        description = "Represents a registered user"

class File(DjangoObjectType):
    class Meta:
        model = FileModel
        description = 'Represents a File object'

class Query(object):
    
    matches = graphene.List(Match, query=graphene.String())
    match = graphene.Field(Match, id=graphene.Int())
    players = graphene.List(Player, query=graphene.String())
    player = graphene.Field(Player, id=graphene.Int())
    playerPositions = graphene.List(PlayerPosition, query=graphene.String())
    playerPosition = graphene.Field(PlayerPosition, id=graphene.Int())
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
            return query(kwargs["query"], MatchModel)
        return MatchModel.objects.all()
    def resolve_match(self, info, id):
        return MatchModel.objects.get(pk=id)
    
    def resolve_players(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], PlayerModel)
        return PlayerModel.objects.all()
    def resolve_player(self, info, id):
        return PlayerModel.objects.get(pk=id)
    
    def resolve_playerPositions(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], PlayerPositionModel)
        return PlayerPositionModel.objects.all()
    def resolve_playerPosition(self, info, id):
        return PlayerPositionModel.objects.get(pk=id)
    
    def resolve_scores(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], ScoreModel)
        return ScoreModel.objects.all()
    def resolve_score(self, info, id):
        return ScoreModel.objects.get(pk=id)
    
    def resolve_teams(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], TeamModel)
        return TeamModel.objects.all()
    def resolve_team(self, info, id):
        return TeamModel.objects.get(pk=id)
    
    def resolve_users(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], UserModel)
        return UserModel.objects.all()
    def resolve_user(self, info, id):
        return UserModel.objects.get(pk=id)
    
    def resolve_files(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], FileModel)
        return FileModel.objects.all()
    def resolve_file(self, info, id):
        return FileModel.objects.get(pk=id)