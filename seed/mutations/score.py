"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Score
from app.models import Player
from app.models import Match
from seed.schema.types import resolve_detail
from seed.schema.types import Score as ScoreTypeField

class SaveScoreMutation(graphene.Mutation):
    
    score = graphene.Field(ScoreTypeField)
    
    class Arguments:
        min = graphene.Int(required=True)
        player = graphene.Int(required=True)
        match = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        score = {}
        if "min" in kwargs:
            score["min"] = kwargs["min"]
        if "player" in kwargs:
            player = resolve_detail(Player, info, kwargs["player"])
            score["player"] = player
        if "match" in kwargs:
            match = resolve_detail(Match, info, kwargs["match"])
            score["match"] = match
        score = \
            Score.objects.create(**score)
        score.save()
    
        return SaveScoreMutation(
            score=score)

class SetScoreMutation(graphene.Mutation):
    
    score = graphene.Field(ScoreTypeField)
    
    class Arguments:
        id = graphene.Int(required=True)
        min = graphene.Int(required=False)
        player = graphene.Int(required=False)
        match = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        score = resolve_detail(Score, info, kwargs["id"])
        if "min" in kwargs:
            score.min = kwargs["min"]
        if "player" in kwargs:
            player = resolve_detail(Player, info, kwargs["player"])
            score.player = player
        if "match" in kwargs:
            match = resolve_detail(Match, info, kwargs["match"])
            score.match = match
        score.save()
    
        return SetScoreMutation(
            score=score)

class DeleteScoreMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        score_id = kwargs["id"]
        score = resolve_detail(Score, info, kwargs["id"])
        score.delete()
        return DeleteScoreMutation(
            id=score_id)