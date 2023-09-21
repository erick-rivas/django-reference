"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

# pylint: disable=C0302
import graphene
import secrets
import math
from graphene import ObjectType
from graphene_django import DjangoListField
from graphene_django.types import DjangoObjectType
from app.models import Match as MatchModel
from app.models import Player as PlayerModel
from app.models import PlayerPosition as PlayerPositionModel
from app.models import Score as ScoreModel
from app.models import Team as TeamModel
from app.models import User as UserModel
from app.models import File as FileModel
from seed.util.query_util import sql_alike_q

class Match(DjangoObjectType):
    id = graphene.Int(description="Match primary key")
    class Meta:
        model = MatchModel
        description = "Represents a match between two teams  (A vs B)"
    def resolve_id(self, info):
        return self.pk

class MatchPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    matches = DjangoListField(Match)

class MatchCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Player(DjangoObjectType):
    id = graphene.Int(description="Player primary key")
    class Meta:
        model = PlayerModel
        
    def resolve_id(self, info):
        return self.pk

class PlayerPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    players = DjangoListField(Player)

class PlayerCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class PlayerPosition(DjangoObjectType):
    id = graphene.Int(description="PlayerPosition primary key")
    class Meta:
        model = PlayerPositionModel
        description = "Represents a player  position (eg. forward)"
    def resolve_id(self, info):
        return self.pk

class PlayerPositionPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    playerPositions = DjangoListField(PlayerPosition)

class PlayerPositionCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Score(DjangoObjectType):
    id = graphene.Int(description="Score primary key")
    class Meta:
        model = ScoreModel
        description = "Represents a match score (goal)"
    def resolve_id(self, info):
        return self.pk

class ScorePagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    scores = DjangoListField(Score)

class ScoreCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Team(DjangoObjectType):
    id = graphene.Int(description="Team primary key")
    class Meta:
        model = TeamModel
        
    def resolve_id(self, info):
        return self.pk

class TeamPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    teams = DjangoListField(Team)

class TeamCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class User(DjangoObjectType):
    id = graphene.Int(description="User primary key")
    class Meta:
        model = UserModel
        exclude = ('password',)
        description = "Represents a registered user"
    def resolve_id(self, info):
        return self.pk

class UserPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    users = DjangoListField(User)

class UserCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class File(DjangoObjectType):
    class Meta:
        model = FileModel
        description = 'Represents a File object'

class FilePagination(ObjectType):
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    files = DjangoListField(File)

class FileCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

def resolve_list(model, info, **kwargs):
    user = info.context.user
    if "query" in kwargs:
        res = model.objects.filter(sql_alike_q(kwargs["query"])).distinct()
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

def resolve_pagination(model, model_name, pagination_type, info, **kwargs):
    total_count = len(resolve_list(model, info, **kwargs))
    total_pages = math.ceil(total_count / kwargs["pageSize"])
    kwargs["start"] = (kwargs["pageNum"] - 1) * kwargs["pageSize"]
    kwargs["end"] = (kwargs["pageNum"]) * kwargs["pageSize"]
    page = resolve_list(model, info, **kwargs)

    return pagination_type(**{
       "id": int(''.join(secrets.choice("0123456789") for i in range(9))),
       "pageNum": kwargs["pageNum"],
       "pageSize": kwargs["pageSize"],
       "totalPages": total_pages,
       "totalCount": total_count,
       model_name: page
    })

def resolve_count(model, count_type, info, **kwargs):
    user = info.context.user
    if "query" in kwargs:
        query = model.objects.filter(sql_alike_q(kwargs["query"])).distinct()
    else:
        query = model.objects.all()
    query = model.filter_permissions(query, model.permission_filters(user))

    return count_type(
        id=int(''.join(secrets.choice("0123456789") for i in range(9))),
        count=len(query))

# pylint: disable=R0904
class Query():
    
    matches = graphene.List(
        Match, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    matchPagination = graphene.Field(
        MatchPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    matchCount = graphene.Field(
        MatchCount, query=graphene.String())
    match = graphene.Field(
        Match, id=graphene.Int(required=True))
    players = graphene.List(
        Player, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    playerPagination = graphene.Field(
        PlayerPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    playerCount = graphene.Field(
        PlayerCount, query=graphene.String())
    player = graphene.Field(
        Player, id=graphene.Int(required=True))
    playerPositions = graphene.List(
        PlayerPosition, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    playerPositionPagination = graphene.Field(
        PlayerPositionPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    playerPositionCount = graphene.Field(
        PlayerPositionCount, query=graphene.String())
    playerPosition = graphene.Field(
        PlayerPosition, id=graphene.Int(required=True))
    scores = graphene.List(
        Score, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    scorePagination = graphene.Field(
        ScorePagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    scoreCount = graphene.Field(
        ScoreCount, query=graphene.String())
    score = graphene.Field(
        Score, id=graphene.Int(required=True))
    teams = graphene.List(
        Team, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    teamPagination = graphene.Field(
        TeamPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    teamCount = graphene.Field(
        TeamCount, query=graphene.String())
    team = graphene.Field(
        Team, id=graphene.Int(required=True))
    users = graphene.List(
        User, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    userPagination = graphene.Field(
        UserPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    userCount = graphene.Field(
        UserCount, query=graphene.String())
    user = graphene.Field(
        User, id=graphene.Int(required=True))
    files = graphene.List(
        File, query=graphene.String(), orderBy=graphene.String(), limit=graphene.Int())
    filePagination = graphene.Field(
        FilePagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    file = graphene.Field(File, id=graphene.Int(required=True))
    fileCount = graphene.Field(FileCount, query=graphene.String())

    # pylint: disable=C0103
    def resolve_matches(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(MatchModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_matchPagination(self, info, **kwargs):
        return resolve_pagination(
            MatchModel, 'matches',
            MatchPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_matchCount(self, info, **kwargs):
        return resolve_count(
          MatchModel, MatchCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_match(self, info, id):
        user = info.context.user
        return MatchModel.filter_permissions(
            MatchModel.objects,
            MatchModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_players(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(PlayerModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_playerPagination(self, info, **kwargs):
        return resolve_pagination(
            PlayerModel, 'players',
            PlayerPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_playerCount(self, info, **kwargs):
        return resolve_count(
          PlayerModel, PlayerCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_player(self, info, id):
        user = info.context.user
        return PlayerModel.filter_permissions(
            PlayerModel.objects,
            PlayerModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_playerPositions(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(PlayerPositionModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_playerPositionPagination(self, info, **kwargs):
        return resolve_pagination(
            PlayerPositionModel, 'playerPositions',
            PlayerPositionPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_playerPositionCount(self, info, **kwargs):
        return resolve_count(
          PlayerPositionModel, PlayerPositionCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_playerPosition(self, info, id):
        user = info.context.user
        return PlayerPositionModel.filter_permissions(
            PlayerPositionModel.objects,
            PlayerPositionModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_scores(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(ScoreModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_scorePagination(self, info, **kwargs):
        return resolve_pagination(
            ScoreModel, 'scores',
            ScorePagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_scoreCount(self, info, **kwargs):
        return resolve_count(
          ScoreModel, ScoreCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_score(self, info, id):
        user = info.context.user
        return ScoreModel.filter_permissions(
            ScoreModel.objects,
            ScoreModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_teams(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(TeamModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_teamPagination(self, info, **kwargs):
        return resolve_pagination(
            TeamModel, 'teams',
            TeamPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_teamCount(self, info, **kwargs):
        return resolve_count(
          TeamModel, TeamCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_team(self, info, id):
        user = info.context.user
        return TeamModel.filter_permissions(
            TeamModel.objects,
            TeamModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_users(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(UserModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_userPagination(self, info, **kwargs):
        return resolve_pagination(
            UserModel, 'users',
            UserPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_userCount(self, info, **kwargs):
        return resolve_count(
          UserModel, UserCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_user(self, info, id):
        user = info.context.user
        return UserModel.filter_permissions(
            UserModel.objects,
            UserModel.permission_filters(user)).get(pk=id)
    
    def resolve_files(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(FileModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_filePagination(self, info, **kwargs):
        return resolve_pagination(FileModel, 'files', FilePagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_fileCount(self, info, **kwargs):
        return resolve_count(FileModel, FileCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_file(self, info, id):
        user = info.context.user
        return FileModel.filter_permissions(
            FileModel.objects, FileModel.permission_filters(user)).get(pk=id)
    pass