"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
import re
from django.db.models import Q
from graphene_django.types import DjangoObjectType
from app.models import Match
from app.models import Player
from app.models import PlayerType
from app.models import Score
from app.models import Team
from app.models import User

def query(data, model):
    data = data.replace(".", "__")
    data = data.replace("(", "")
    data = data.replace(")", "")
    res = Q()
    queries = [i.strip() for i in data.split("||")]
    for q in queries:
        filters = [i.strip() for i in q.split("&&")]
        values = {}
        for f in filters:
            ele = f.split("=")
            values[ele[0].strip()] = ele[1].strip()
        res |= Q(**values)
    return model.objects.filter(res)

class _MatchType(DjangoObjectType):
    class Meta:
        model = Match

class _PlayerType(DjangoObjectType):
    class Meta:
        model = Player

class _PlayerTypeType(DjangoObjectType):
    class Meta:
        model = PlayerType

class _ScoreType(DjangoObjectType):
    class Meta:
        model = Score

class _TeamType(DjangoObjectType):
    class Meta:
        model = Team

class _UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ('password',)

class Query(object):
    matches = graphene.List(_MatchType, query=graphene.String())
    match = graphene.Field(_MatchType, id=graphene.Int())
    players = graphene.List(_PlayerType, query=graphene.String())
    player = graphene.Field(_PlayerType, id=graphene.Int())
    playerTypes = graphene.List(_PlayerTypeType, query=graphene.String())
    playerType = graphene.Field(_PlayerTypeType, id=graphene.Int())
    scores = graphene.List(_ScoreType, query=graphene.String())
    score = graphene.Field(_ScoreType, id=graphene.Int())
    teams = graphene.List(_TeamType, query=graphene.String())
    team = graphene.Field(_TeamType, id=graphene.Int())
    users = graphene.List(_UserType, query=graphene.String())
    user = graphene.Field(_UserType, id=graphene.Int())
    
    def resolve_matches(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], Match)
        return Match.objects.all()
    def resolve_match(self, info, id):
        return Match.objects.get(pk=id)
    def resolve_players(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], Player)
        return Player.objects.all()
    def resolve_player(self, info, id):
        return Player.objects.get(pk=id)
    def resolve_playerTypes(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], PlayerType)
        return PlayerType.objects.all()
    def resolve_playerType(self, info, id):
        return PlayerType.objects.get(pk=id)
    def resolve_scores(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], Score)
        return Score.objects.all()
    def resolve_score(self, info, id):
        return Score.objects.get(pk=id)
    def resolve_teams(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], Team)
        return Team.objects.all()
    def resolve_team(self, info, id):
        return Team.objects.get(pk=id)
    def resolve_users(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], User)
        return User.objects.all()
    def resolve_user(self, info, id):
        return User.objects.get(pk=id)