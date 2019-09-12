"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene

import seed.schema.types
import seed.mutations.match
import seed.mutations.player
import seed.mutations.player_type
import seed.mutations.score
import seed.mutations.team
import seed.mutations.user

class _Query(seed.schema.types.Query, graphene.ObjectType):
    pass

class _Mutation(graphene.ObjectType):
    matches = seed.mutations.match.MatchMutation.Field()
    players = seed.mutations.player.PlayerMutation.Field()
    playerTypes = seed.mutations.player_type.PlayerTypeMutation.Field()
    scores = seed.mutations.score.ScoreMutation.Field()
    teams = seed.mutations.team.TeamMutation.Field()
    users = seed.mutations.user.UserMutation.Field()
