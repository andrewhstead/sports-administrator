from datetime import date
from django.db import models
from data.models import Country, Competition, Season

# Create your models here.
class Edition(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    competition = models.ForeignKey(Competition, related_name='editions', on_delete=models.CASCADE)
    season = models.ForeignKey(Season, related_name='editions', on_delete=models.CASCADE, unique=True)
    is_current = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Club(models.Model):
    objects = models.Manager()
    full_name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=15, unique=True)
    abbreviation = models.CharField(max_length=3, unique=True)
    country = models.ForeignKey(Country, related_name='clubs', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class ClubRecord(models.Model):
    objects = models.Manager()
    season = models.ForeignKey(Season, related_name='club', on_delete=models.CASCADE, unique=True)
    full_name = models.CharField(max_length=50)
    club = models.ForeignKey(Club, related_name='club_years', on_delete=models.CASCADE)
    short_name = models.CharField(max_length=15)
    abbreviation = models.CharField(max_length=3)

    def __str__(self):
        return self.full_name


class Player(models.Model):
    objects = models.Manager()
    first_name = models.CharField(max_length=25)
    middle_names = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=date.today)
    place_of_birth = models.CharField(max_length=50, blank=True, null=True)
    country = models.ForeignKey(Country, related_name='players', on_delete=models.CASCADE, blank=True, null=True)
    current_club = models.ForeignKey(Club, related_name='current_players', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.full_name


class PlayerRecord(models.Model):
    objects = models.Manager()
    player = models.ForeignKey(Player, related_name='player_years', on_delete=models.CASCADE)
    season = models.ForeignKey(Season, related_name='player', on_delete=models.CASCADE)
    club = models.ForeignKey(Club, related_name='players', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name