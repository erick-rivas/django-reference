"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
import random
from graphene import ObjectType
from graphene_django.types import DjangoObjectType
from app.models import Match as MatchModel
from app.models import Player as PlayerModel
from app.models import PlayerPosition as PlayerPositionModel
from app.models import Score as ScoreModel
from app.models import Team as TeamModel
from app.models import User as UserModel
from app.models import File as FileModel
from seed.util.query_util import sql_alike_Q

class Match(DjangoObjectType):
    id = graphene.Int(description = "Match primary key")
    class Meta:
        model = MatchModel
        description = "Represents a match between two teams  (A vs B)"
    def resolve_id(self, info):
        return self.pk

class MatchCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Player(DjangoObjectType):
    id = graphene.Int(description = "Player primary key")
    class Meta:
        model = PlayerModel
        
    def resolve_id(self, info):
        return self.pk

class PlayerCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class PlayerPosition(DjangoObjectType):
    id = graphene.Int(description = "PlayerPosition primary key")
    class Meta:
        model = PlayerPositionModel
        description = "Represents a player  position (eg. forward)"
    def resolve_id(self, info):
        return self.pk

class PlayerPositionCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Score(DjangoObjectType):
    id = graphene.Int(description = "Score primary key")
    class Meta:
        model = ScoreModel
        description = "Represents a match score (goal)"
    def resolve_id(self, info):
        return self.pk

class ScoreCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Team(DjangoObjectType):
    id = graphene.Int(description = "Team primary key")
    class Meta:
        model = TeamModel
        
    def resolve_id(self, info):
        return self.pk

class TeamCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class User(DjangoObjectType):
    id = graphene.Int(description = "User primary key")
    class Meta:
        model = UserModel
        exclude = ('password',)
        description = "Represents a registered user"
    def resolve_id(self, info):
        return self.pk

class UserCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class File(DjangoObjectType):
    class Meta:
        model = FileModel
        description = 'Represents a File object'

class FileCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

def resolve_list(model, info, **kwargs):
    user = info.context.user
    if "query" in kwargs:
        res = model.objects.filter(sql_alike_Q(kwargs["query"])).distinct()
    else:
        res = model.objects.all()
    if "orderBy" in kwargs:
        orders = kwargs["orderBy"].split(",")
        for order in orders:
            res = res.order_by(order)
    if "start" in kwargs and "end" not in kwargs:
        res = res[kwargs["start"]:]
    if "end" in kwargs and "start" not in kwargs:
        res = res[:kwargs["end"]]
    if "start" in kwargs and "end" in kwargs:
        res = res[kwargs["start"]:kwargs["end"]]
    res = model.filter_permissions(res, model.permission_filters(user))
    return res

def resolve_count(model, countType, info, **kwargs):
    user = info.context.user
    if "query" in kwargs:
        query = model.objects.filter(sql_alike_Q(kwargs["query"])).distinct()
    else:
        query = model.objects.all()
    query = model.filter_permissions(query, model.permission_filters(user))

    return countType(
        id=random.randint(0, 1000000),
        count=len(query))

class Query(object):
    
    matches = graphene.List(Match, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    matchCount = graphene.Field(MatchCount, query=graphene.String())
    match = graphene.Field(Match, id=graphene.Int())
    players = graphene.List(Player, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    playerCount = graphene.Field(PlayerCount, query=graphene.String())
    player = graphene.Field(Player, id=graphene.Int())
    playerPositions = graphene.List(PlayerPosition, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    playerPositionCount = graphene.Field(PlayerPositionCount, query=graphene.String())
    playerPosition = graphene.Field(PlayerPosition, id=graphene.Int())
    scores = graphene.List(Score, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    scoreCount = graphene.Field(ScoreCount, query=graphene.String())
    score = graphene.Field(Score, id=graphene.Int())
    teams = graphene.List(Team, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    teamCount = graphene.Field(TeamCount, query=graphene.String())
    team = graphene.Field(Team, id=graphene.Int())
    users = graphene.List(User, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    userCount = graphene.Field(UserCount, query=graphene.String())
    user = graphene.Field(User, id=graphene.Int())
    files = graphene.List(File, query=graphene.String(), orderBy=graphene.String(),
      start=graphene.Int(), end=graphene.Int())
    file = graphene.Field(File, id=graphene.Int())
    fileCount = graphene.Field(FileCount, query=graphene.String())

    def resolve_matches(self, info, **kwargs):
        return resolve_list(MatchModel, info, **kwargs)

    def resolve_matchCount(self, info, **kwargs):
        return resolve_count(MatchModel, MatchCount, info, **kwargs)

    def resolve_match(self, info, id):
        user = info.context.user
        return MatchModel.filter_permissions(MatchModel.objects, MatchModel.permission_filters(user)).get(pk=id)
    
    def resolve_players(self, info, **kwargs):
        return resolve_list(PlayerModel, info, **kwargs)

    def resolve_playerCount(self, info, **kwargs):
        return resolve_count(PlayerModel, PlayerCount, info, **kwargs)

    def resolve_player(self, info, id):
        user = info.context.user
        return PlayerModel.filter_permissions(PlayerModel.objects, PlayerModel.permission_filters(user)).get(pk=id)
    
    def resolve_playerPositions(self, info, **kwargs):
        return resolve_list(PlayerPositionModel, info, **kwargs)

    def resolve_playerPositionCount(self, info, **kwargs):
        return resolve_count(PlayerPositionModel, PlayerPositionCount, info, **kwargs)

    def resolve_playerPosition(self, info, id):
        user = info.context.user
        return PlayerPositionModel.filter_permissions(PlayerPositionModel.objects, PlayerPositionModel.permission_filters(user)).get(pk=id)
    
    def resolve_scores(self, info, **kwargs):
        return resolve_list(ScoreModel, info, **kwargs)

    def resolve_scoreCount(self, info, **kwargs):
        return resolve_count(ScoreModel, ScoreCount, info, **kwargs)

    def resolve_score(self, info, id):
        user = info.context.user
        return ScoreModel.filter_permissions(ScoreModel.objects, ScoreModel.permission_filters(user)).get(pk=id)
    
    def resolve_teams(self, info, **kwargs):
        return resolve_list(TeamModel, info, **kwargs)

    def resolve_teamCount(self, info, **kwargs):
        return resolve_count(TeamModel, TeamCount, info, **kwargs)

    def resolve_team(self, info, id):
        user = info.context.user
        return TeamModel.filter_permissions(TeamModel.objects, TeamModel.permission_filters(user)).get(pk=id)
    
    def resolve_users(self, info, **kwargs):
        return resolve_list(UserModel, info, **kwargs)

    def resolve_userCount(self, info, **kwargs):
        return resolve_count(UserModel, UserCount, info, **kwargs)

    def resolve_user(self, info, id):
        user = info.context.user
        return UserModel.filter_permissions(UserModel.objects, UserModel.permission_filters(user)).get(pk=id)
    
    def resolve_files(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            res = FileModel.objects.filter(sql_alike_Q(kwargs["query"])).distinct()
        else: res = FileModel.objects.all()
        if "orderBy" in kwargs:
            orders = kwargs["orderBy"].split(",")
            for order in orders:
              res = res.order_by(order)
        if "start" in kwargs and "end" not in kwargs:
            res = res[kwargs["start"]:]
        if "end" in kwargs and "start" not in kwargs:
            res = res[:kwargs["end"]]
        if "start" in kwargs and "end" in kwargs:
            res = res[kwargs["start"]:kwargs["end"]]
        res = FileModel.filter_permissions(res, FileModel.permission_filters(user))
        return res

    def resolve_fileCount(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            return FileCount(
                id = 0,
                count=len(FileModel.objects.filter(sql_alike_Q(kwargs["query"])).distinct()))
        else:
            return FileCount(
                id = 0,
                count=len(FileModel.filter_permissions(FileModel.objects.all(), FileModel.permission_filters(user))))

    def resolve_file(self, info, id):
        user = info.context.user
        return FileModel.filter_permissions(FileModel.objects, FileModel.permission_filters(user)).get(pk=id)
    pass