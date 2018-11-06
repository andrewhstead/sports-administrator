from django.contrib import admin
from .models import Edition, Club, ClubSeason, LeagueRecord, Player, PlayerRecord, Game

# Register your models here.
admin.site.register(Edition)
admin.site.register(Club)
admin.site.register(ClubSeason)
admin.site.register(LeagueRecord)
admin.site.register(Player)
admin.site.register(PlayerRecord)
admin.site.register(Game)