"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Score
from app.models import Player
from app.models import Match
from app.models import File
from seed.schema.types import Score as ScoreType

class SaveScoreMutation(graphene.Mutation):
    
    score = graphene.Field(ScoreType)
    
    class Arguments:
        min = graphene.Int(required=True)
        player = graphene.Int(required=True)
        match = graphene.Int(required=True)

    def mutate(self, info, **kwargs):

        score = {}
        if "min" in kwargs: score["min"] = kwargs["min"]
        if "player" in kwargs:
             player = Player.objects.get(pk = kwargs["player"])
             score["player"] = player
        if "match" in kwargs:
             match = Match.objects.get(pk = kwargs["match"])
             score["match"] = match
        score = Score.objects.create(**score)
        score.save()
    
        return SaveScoreMutation(score=score)

class SetScoreMutation(graphene.Mutation):
    
    score = graphene.Field(ScoreType)
    
    class Arguments:
        id = graphene.Int(required=True)
        min = graphene.Int(required=False)
        player = graphene.Int(required=False)
        match = graphene.Int(required=False)

    def mutate(self, info, **kwargs):

        score = Score.objects.get(pk=kwargs["id"])
        if "min" in kwargs: score.min = kwargs["min"]
        if "player" in kwargs:
             player = Player.objects.get(pk = kwargs["player"])
             score.player = player
        if "match" in kwargs:
             match = Match.objects.get(pk = kwargs["match"])
             score.match = match
        score.save()
    
        return SetScoreMutation(score=score)

class DeleteScoreMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        score = Score.objects.get(pk=kwargs["id"])
        score.delete()
        return DeleteScoreMutation(id=id)
