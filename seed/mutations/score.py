"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import Score
from app.models import Player
from app.models import Match
from seed.schema.types import _ScoreType

class ScoreMutation(graphene.Mutation):
    score = graphene.Field(_ScoreType)
    class Arguments:
        id = graphene.Int(required=False)
        min = graphene.Int(required=False)
        playerId = graphene.Int(required=False)
        matchId = graphene.Int(required=False)

    def mutate(self, info, **kwargs):

        score = None
        if "id" in kwargs:
            score = Score.objects.get(pk=kwargs["id"])
            if "min" in kwargs: score.min = kwargs["min"]
            if "playerId" in kwargs: 
                player = Player.objects.get(pk = kwargs["playerId"])
                score.player = player
            if "matchId" in kwargs: 
                match = Match.objects.get(pk = kwargs["matchId"])
                score.match = match
        else:
            player = Player.objects.get(pk = kwargs["playerId"])
            match = Match.objects.get(pk = kwargs["matchId"])
            score = Score.objects.create(
                min = kwargs["min"],
                player = player,
                match = match,
            )
        score.save()
    
        return ScoreMutation(score=score)
