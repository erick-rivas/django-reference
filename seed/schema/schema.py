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
    
    saveMatch = seed.mutations.match.SaveMatchMutation.Field()
    setMatch = seed.mutations.match.SetMatchMutation.Field()
    deleteMatch = seed.mutations.match.DeleteMatchMutation.Field()
    savePlayer = seed.mutations.player.SavePlayerMutation.Field()
    setPlayer = seed.mutations.player.SetPlayerMutation.Field()
    deletePlayer = seed.mutations.player.DeletePlayerMutation.Field()
    savePlayerType = seed.mutations.player_type.SavePlayerTypeMutation.Field()
    setPlayerType = seed.mutations.player_type.SetPlayerTypeMutation.Field()
    deletePlayerType = seed.mutations.player_type.DeletePlayerTypeMutation.Field()
    saveScore = seed.mutations.score.SaveScoreMutation.Field()
    setScore = seed.mutations.score.SetScoreMutation.Field()
    deleteScore = seed.mutations.score.DeleteScoreMutation.Field()
    saveTeam = seed.mutations.team.SaveTeamMutation.Field()
    setTeam = seed.mutations.team.SetTeamMutation.Field()
    deleteTeam = seed.mutations.team.DeleteTeamMutation.Field()
    saveUser = seed.mutations.user.SaveUserMutation.Field()
    setUser = seed.mutations.user.SetUserMutation.Field()
    deleteUser = seed.mutations.user.DeleteUserMutation.Field()

