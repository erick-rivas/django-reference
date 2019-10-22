"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_match():
    from seed.models.match import Match
    return Match

def get_player():
    from seed.models.player import Player
    return Player

def get_player_position():
    from seed.models.player_position import PlayerPosition
    return PlayerPosition

def get_score():
    from seed.models.score import Score
    return Score

def get_team():
    from seed.models.team import Team
    return Team

def get_user():
    from seed.models.user import User
    return User

def get_file():
    from seed.models.helpers.file import File
    return File

Match = get_match()
Player = get_player()
PlayerPosition = get_player_position()
Score = get_score()
Team = get_team()
User = get_user()
File = get_file()
