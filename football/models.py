from datetime import date
from django.db import models
from data.models import Country, Competition, Season
from django.utils import timezone
now = timezone.now

# Options for club status in league table.
STATUS_OPTIONS = (
    ('c', "Champions"),
    ('p', "Promoted"),
    ('r', "Relegated"),
    ('po', "Play-Offs"),
    ('ppo', "Promoted after Play-Offs"),
    ('rpo', "Relegated after Play-Offs"),
)

# Create your models here.
class Club(models.Model):
    objects = models.Manager()
    full_name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=15, unique=True)
    abbreviation = models.CharField(max_length=3, unique=True)
    country = models.ForeignKey(Country, related_name='clubs', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="images/logos", blank=True, null=True)
    current_league = models.ForeignKey(Competition, related_name='clubs', on_delete=models.CASCADE, blank=True, null=True)
    primary_color = models.CharField(max_length=10, blank=True, null=True, default="#ffffff")
    secondary_color = models.CharField(max_length=10, blank=True, null=True, default="#ffffff")
    primary_text = models.CharField(max_length=10, blank=True, null=True, default="#000000")
    secondary_text = models.CharField(max_length=10, blank=True, null=True, default="#000000")
    date_modified = models.DateTimeField(default=now)
    slug = models.SlugField(default='')

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
    image = models.ImageField(upload_to="images/players", blank=True, null=True)
    date_modified = models.DateTimeField(default=now)

    def __str__(self):
        return self.last_name


class PlayerRecord(models.Model):
    objects = models.Manager()
    player = models.ForeignKey(Player, related_name='player_years', on_delete=models.CASCADE)
    season = models.ForeignKey(Season, related_name='player', on_delete=models.CASCADE)
    club = models.ForeignKey(Club, related_name='players', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
        
        
class Edition(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    competition = models.ForeignKey(Competition, related_name='editions', on_delete=models.CASCADE)
    teams = models.ManyToManyField(Club, related_name='edition', blank=True)
    season = models.ForeignKey(Season, related_name='editions', on_delete=models.CASCADE, unique=True)
    is_current = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ClubSeason(models.Model):
    objects = models.Manager()
    club = models.ForeignKey(Club, related_name='club_years', on_delete=models.CASCADE)
    season = models.ForeignKey(Season, related_name='club', on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    short_name = models.CharField(max_length=15, blank=True, null=True)
    abbreviation = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.full_name


class LeagueRecord(models.Model):
    objects = models.Manager()
    clubseason = models.ForeignKey(ClubSeason, related_name='league', on_delete=models.CASCADE, blank=True, null=True)
    edition = models.ForeignKey(Edition, related_name='team', on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    position = models.IntegerField(default=1)
    total_played = models.IntegerField(default=0)
    total_won = models.IntegerField(default=0)
    total_drawn = models.IntegerField(default=0)
    total_lost = models.IntegerField(default=0)
    total_for = models.IntegerField(default=0)
    total_against = models.IntegerField(default=0)
    home_played = models.IntegerField(default=0)
    home_won = models.IntegerField(default=0)
    home_drawn = models.IntegerField(default=0)
    home_lost = models.IntegerField(default=0)
    home_for = models.IntegerField(default=0)
    home_against = models.IntegerField(default=0)
    away_played = models.IntegerField(default=0)
    away_won = models.IntegerField(default=0)
    away_drawn = models.IntegerField(default=0)
    away_lost = models.IntegerField(default=0)
    away_for = models.IntegerField(default=0)
    away_against = models.IntegerField(default=0)
    table_tiebreaker = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    adjustment = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=STATUS_OPTIONS, blank=True, null=True)

    def __obj__(self):
        return self.clubseason