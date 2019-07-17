"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_player():
    from models.player import Player
    return Player

def get_team():
    from models.team import Team
    return Team

def get_user():
    from models.user import User
    return User

def get_match():
    from models.stats.match import Match
    return Match

def get_score():
    from models.stats.score import Score
    return Score

def get_file():
    from models.helpers.file import File
    return File

Player = get_player()
Team = get_team()
User = get_user()
Match = get_match()
Score = get_score()
File = get_file()
