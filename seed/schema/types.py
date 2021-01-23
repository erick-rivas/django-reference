"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
import random
from graphene import ObjectType
from graphene_django.types import DjangoObjectType
from seed.schema.util.query_util import parse_query
from app.models import Match as MatchModel
from app.models import Player as PlayerModel
from app.models import PlayerPosition as PlayerPositionModel
from app.models import Score as ScoreModel
from app.models import Team as TeamModel
from app.models import User as UserModel
from app.models import File as FileModel

class Match(DjangoObjectType):
    class Meta:
        model = MatchModel
        description = "Represents a match between two teams  (A vs B)"

class MatchCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Player(DjangoObjectType):
    class Meta:
        model = PlayerModel

class PlayerCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class PlayerPosition(DjangoObjectType):
    class Meta:
        model = PlayerPositionModel
        description = "Represents a player  position (eg. forward)"

class PlayerPositionCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Score(DjangoObjectType):
    class Meta:
        model = ScoreModel
        description = "Represents a match score (goal)"

class ScoreCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Team(DjangoObjectType):
    class Meta:
        model = TeamModel

class TeamCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class User(DjangoObjectType):
    class Meta:
        model = UserModel
        exclude = ('password',)
        description = "Represents a registered user"

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
        user = info.context.user
        if "query" in kwargs:
            res = parse_query(kwargs["query"], MatchModel)
        else: res = MatchModel.filter_permissions(MatchModel.objects.all(), MatchModel.permission_filters(user))
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
        res = MatchModel.filter_permissions(res, MatchModel.permission_filters(user))
        return res

    def resolve_matchCount(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            return MatchCount(
                id = random.randint(0, 1000000),
                count=len(parse_query(kwargs["query"], MatchModel)))
        else:
            return MatchCount(
                id = random.randint(0, 1000000),
                count=len(MatchModel.filter_permissions(MatchModel.objects.all(), MatchModel.permission_filters(user))))

    def resolve_match(self, info, id):
        user = info.context.user
        return MatchModel.filter_permissions(MatchModel.objects, MatchModel.permission_filters(user)).get(pk=id)
    
    def resolve_players(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            res = parse_query(kwargs["query"], PlayerModel)
        else: res = PlayerModel.filter_permissions(PlayerModel.objects.all(), PlayerModel.permission_filters(user))
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
        res = PlayerModel.filter_permissions(res, PlayerModel.permission_filters(user))
        return res

    def resolve_playerCount(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            return PlayerCount(
                id = random.randint(0, 1000000),
                count=len(parse_query(kwargs["query"], PlayerModel)))
        else:
            return PlayerCount(
                id = random.randint(0, 1000000),
                count=len(PlayerModel.filter_permissions(PlayerModel.objects.all(), PlayerModel.permission_filters(user))))

    def resolve_player(self, info, id):
        user = info.context.user
        return PlayerModel.filter_permissions(PlayerModel.objects, PlayerModel.permission_filters(user)).get(pk=id)
    
    def resolve_playerPositions(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            res = parse_query(kwargs["query"], PlayerPositionModel)
        else: res = PlayerPositionModel.filter_permissions(PlayerPositionModel.objects.all(), PlayerPositionModel.permission_filters(user))
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
        res = PlayerPositionModel.filter_permissions(res, PlayerPositionModel.permission_filters(user))
        return res

    def resolve_playerPositionCount(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            return PlayerPositionCount(
                id = random.randint(0, 1000000),
                count=len(parse_query(kwargs["query"], PlayerPositionModel)))
        else:
            return PlayerPositionCount(
                id = random.randint(0, 1000000),
                count=len(PlayerPositionModel.filter_permissions(PlayerPositionModel.objects.all(), PlayerPositionModel.permission_filters(user))))

    def resolve_playerPosition(self, info, id):
        user = info.context.user
        return PlayerPositionModel.filter_permissions(PlayerPositionModel.objects, PlayerPositionModel.permission_filters(user)).get(pk=id)
    
    def resolve_scores(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            res = parse_query(kwargs["query"], ScoreModel)
        else: res = ScoreModel.filter_permissions(ScoreModel.objects.all(), ScoreModel.permission_filters(user))
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
        res = ScoreModel.filter_permissions(res, ScoreModel.permission_filters(user))
        return res

    def resolve_scoreCount(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            return ScoreCount(
                id = random.randint(0, 1000000),
                count=len(parse_query(kwargs["query"], ScoreModel)))
        else:
            return ScoreCount(
                id = random.randint(0, 1000000),
                count=len(ScoreModel.filter_permissions(ScoreModel.objects.all(), ScoreModel.permission_filters(user))))

    def resolve_score(self, info, id):
        user = info.context.user
        return ScoreModel.filter_permissions(ScoreModel.objects, ScoreModel.permission_filters(user)).get(pk=id)
    
    def resolve_teams(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            res = parse_query(kwargs["query"], TeamModel)
        else: res = TeamModel.filter_permissions(TeamModel.objects.all(), TeamModel.permission_filters(user))
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
        res = TeamModel.filter_permissions(res, TeamModel.permission_filters(user))
        return res

    def resolve_teamCount(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            return TeamCount(
                id = random.randint(0, 1000000),
                count=len(parse_query(kwargs["query"], TeamModel)))
        else:
            return TeamCount(
                id = random.randint(0, 1000000),
                count=len(TeamModel.filter_permissions(TeamModel.objects.all(), TeamModel.permission_filters(user))))

    def resolve_team(self, info, id):
        user = info.context.user
        return TeamModel.filter_permissions(TeamModel.objects, TeamModel.permission_filters(user)).get(pk=id)
    
    def resolve_users(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            res = parse_query(kwargs["query"], UserModel)
        else: res = UserModel.filter_permissions(UserModel.objects.all(), UserModel.permission_filters(user))
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
        res = UserModel.filter_permissions(res, UserModel.permission_filters(user))
        return res

    def resolve_userCount(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            return UserCount(
                id = random.randint(0, 1000000),
                count=len(parse_query(kwargs["query"], UserModel)))
        else:
            return UserCount(
                id = random.randint(0, 1000000),
                count=len(UserModel.filter_permissions(UserModel.objects.all(), UserModel.permission_filters(user))))

    def resolve_user(self, info, id):
        user = info.context.user
        return UserModel.filter_permissions(UserModel.objects, UserModel.permission_filters(user)).get(pk=id)
    
    def resolve_files(self, info, **kwargs):
        user = info.context.user
        if "query" in kwargs:
            res = parse_query(kwargs["query"], FileModel)
        else: res = FileModel.filter_permissions(FileModel.objects.all(), FileModel.permission_filters(user))
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
                count=len(parse_query(kwargs["query"], FileModel)))
        else:
            return FileCount(
                id = 0,
                count=len(FileModel.filter_permissions(FileModel.objects.all(), FileModel.permission_filters(user))))

    def resolve_file(self, info, id):
        user = info.context.user
        return FileModel.filter_permissions(FileModel.objects, FileModel.permission_filters(user)).get(pk=id)
    pass