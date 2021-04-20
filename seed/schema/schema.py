"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""
import graphene

import seed.schema.types
import seed.mutations.match
import seed.mutations.player
import seed.mutations.player_position
import seed.mutations.score
import seed.mutations.team
import seed.mutations.user

class Query(seed.schema.types.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    
    saveMatch = seed.mutations.match.SaveMatchMutation.Field()
    setMatch = seed.mutations.match.SetMatchMutation.Field()
    deleteMatch = seed.mutations.match.DeleteMatchMutation.Field()
    savePlayer = seed.mutations.player.SavePlayerMutation.Field()
    setPlayer = seed.mutations.player.SetPlayerMutation.Field()
    deletePlayer = seed.mutations.player.DeletePlayerMutation.Field()
    savePlayerPosition = seed.mutations.player_position.SavePlayerPositionMutation.Field()
    setPlayerPosition = seed.mutations.player_position.SetPlayerPositionMutation.Field()
    deletePlayerPosition = seed.mutations.player_position.DeletePlayerPositionMutation.Field()
    saveScore = seed.mutations.score.SaveScoreMutation.Field()
    setScore = seed.mutations.score.SetScoreMutation.Field()
    deleteScore = seed.mutations.score.DeleteScoreMutation.Field()
    saveTeam = seed.mutations.team.SaveTeamMutation.Field()
    setTeam = seed.mutations.team.SetTeamMutation.Field()
    deleteTeam = seed.mutations.team.DeleteTeamMutation.Field()
    saveUser = seed.mutations.user.SaveUserMutation.Field()
    setUser = seed.mutations.user.SetUserMutation.Field()
    deleteUser = seed.mutations.user.DeleteUserMutation.Field()
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)