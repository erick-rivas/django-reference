from django.contrib import admin

from models.match import Match
from models.player import  Player
from models.score import  Score
from models.team import Team

admin.site.register(Match)
admin.site.register(Player)
admin.site.register(Score)
admin.site.register(Team)
