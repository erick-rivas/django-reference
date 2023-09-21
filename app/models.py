"""
__Seed builder__
  AUTO_GENERATED Proxy (Read only)
  Modify via builder
"""

def get_match():
    import seed.models.match as SeedModel
    return SeedModel.Match

def get_player():
    import seed.models.player as SeedModel
    return SeedModel.Player

def get_player_position():
    import seed.models.player_position as SeedModel
    return SeedModel.PlayerPosition

def get_score():
    import seed.models.score as SeedModel
    return SeedModel.Score

def get_team():
    import seed.models.team as SeedModel
    return SeedModel.Team

def get_user():
    import seed.models.user as SeedModel
    return SeedModel.User

def get_file():
    import seed.models.file as SeedFile
    return SeedFile.File

Match = get_match()
Player = get_player()
PlayerPosition = get_player_position()
Score = get_score()
Team = get_team()
User = get_user()
File = get_file()