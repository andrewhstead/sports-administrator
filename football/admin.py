from django.contrib import admin
from .models import Edition, Club, ClubRecord, Player, PlayerRecord

# Register your models here.
admin.site.register(Edition)
admin.site.register(Club)
admin.site.register(ClubRecord)
admin.site.register(Player)
admin.site.register(PlayerRecord)