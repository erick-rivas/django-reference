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
    
    createMatch = seed.mutations.match.CreateMatchMutation.Field()
    updateMatch = seed.mutations.match.UpdateMatchMutation.Field()
    deleteMatch = seed.mutations.match.DeleteMatchMutation.Field()
    createPlayer = seed.mutations.player.CreatePlayerMutation.Field()
    updatePlayer = seed.mutations.player.UpdatePlayerMutation.Field()
    deletePlayer = seed.mutations.player.DeletePlayerMutation.Field()
    createPlayerType = seed.mutations.player_type.CreatePlayerTypeMutation.Field()
    updatePlayerType = seed.mutations.player_type.UpdatePlayerTypeMutation.Field()
    deletePlayerType = seed.mutations.player_type.DeletePlayerTypeMutation.Field()
    createScore = seed.mutations.score.CreateScoreMutation.Field()
    updateScore = seed.mutations.score.UpdateScoreMutation.Field()
    deleteScore = seed.mutations.score.DeleteScoreMutation.Field()
    createTeam = seed.mutations.team.CreateTeamMutation.Field()
    updateTeam = seed.mutations.team.UpdateTeamMutation.Field()
    deleteTeam = seed.mutations.team.DeleteTeamMutation.Field()
    createUser = seed.mutations.user.CreateUserMutation.Field()
    updateUser = seed.mutations.user.UpdateUserMutation.Field()
    deleteUser = seed.mutations.user.DeleteUserMutation.Field()

