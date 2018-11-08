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

# The options for game status which are available in the administration area.
GAME_STATUS = (
    ('scheduled', "Scheduled"),
    ('completed', "Completed"),
    ('in_progress', "In Progress"),
    ('postponed', "postponed"),
)

# The options for tie-breakers which can be used in leagues.
TIE_BREAKERS = (
    ('Goal Average', "Goal Average"),
    ('Goal Difference', "Goal Difference"),
    ('Goals For', "Goals For"),
    ('Games Won', "Games Won"),
    ('Name', "Name"),
)

# Options for the result of a game.
RESULT_CHOICES = (
    ('H', "Home Win"),
    ('A', "Away Win"),
    ('D', "Draw"),
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
	# Set up the league's points system and other rules.
    home_win_points = models.IntegerField(default=3)
    away_win_points = models.IntegerField(default=3)
    home_draw_points = models.IntegerField(default=1)
    away_draw_points = models.IntegerField(default=1)
    home_loss_points = models.IntegerField(default=0)
    away_loss_points = models.IntegerField(default=0)
    named_substitutes = models.IntegerField(default=5)
	# Tie breakers default to 'Name' to ensure alphabetical sorting once all other criteria have been applied.
    tie_breaker_1 = models.CharField(max_length=25, choices=TIE_BREAKERS, default="Name")
    tie_breaker_2 = models.CharField(max_length=25, choices=TIE_BREAKERS, default="Name")
    tie_breaker_3 = models.CharField(max_length=25, choices=TIE_BREAKERS, default="Name")
    tie_breaker_4 = models.CharField(max_length=25, choices=TIE_BREAKERS, default="Name")
    tie_breaker_5 = models.CharField(max_length=25, choices=TIE_BREAKERS, default="Name")
	# Places to indicate promotion and relegation issues etc.
    top_primary_places = models.PositiveIntegerField(default=0)
    top_secondary_places = models.PositiveIntegerField(default=0)
    bottom_primary_places = models.PositiveIntegerField(default=0)
    bottom_secondary_places = models.PositiveIntegerField(default=0)
	# Text field for explanatory notes.
    note = models.TextField(blank=True, null=True)

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
        return self.full_name + " " + self.season.name


class LeagueRecord(models.Model):
    objects = models.Manager()
    clubseason = models.ForeignKey(ClubSeason, related_name='league', on_delete=models.CASCADE, blank=True, null=True)
    edition = models.ForeignKey(Edition, related_name='team', on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    position = models.PositiveIntegerField(default=1)
    total_played = models.PositiveIntegerField(default=0)
    total_won = models.PositiveIntegerField(default=0)
    total_drawn = models.PositiveIntegerField(default=0)
    total_lost = models.PositiveIntegerField(default=0)
    total_for = models.PositiveIntegerField(default=0)
    total_against = models.PositiveIntegerField(default=0)
    home_played = models.PositiveIntegerField(default=0)
    home_won = models.PositiveIntegerField(default=0)
    home_drawn = models.PositiveIntegerField(default=0)
    home_lost = models.PositiveIntegerField(default=0)
    home_for = models.PositiveIntegerField(default=0)
    home_against = models.PositiveIntegerField(default=0)
    away_played = models.PositiveIntegerField(default=0)
    away_won = models.PositiveIntegerField(default=0)
    away_drawn = models.PositiveIntegerField(default=0)
    away_lost = models.PositiveIntegerField(default=0)
    away_for = models.PositiveIntegerField(default=0)
    away_against = models.PositiveIntegerField(default=0)
    table_tiebreaker = models.IntegerField(default=0)
    total_points = models.PositiveIntegerField(default=0)
    adjustment = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=STATUS_OPTIONS, blank=True, null=True)

    def __str__(self):
        return self.full_name + ": " + self.edition.season.name


# Game model for individual matches.
class Game(models.Model):
    objects = models.Manager()
    edition = models.ForeignKey(Edition, related_name='games', on_delete=models.CASCADE)
    game_status = models.CharField(max_length=10, choices=GAME_STATUS, default="Scheduled")
    game_date = models.DateField(default=date.today)
    game_time = models.TimeField(blank=True, null=True)
    neutral_venue = models.BooleanField(default=False)
    home_team = models.ForeignKey(Club, related_name='game_home', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Club, related_name='game_away', on_delete=models.CASCADE)
    home_score = models.PositiveIntegerField(blank=True, null=True)
    away_score = models.PositiveIntegerField(blank=True, null=True)
    result = models.CharField(max_length=1, choices=RESULT_CHOICES, blank=True, null=True)
    attendance = models.PositiveIntegerField(blank=True, null=True)
    date_modified = models.DateTimeField(default=now)
    # Statistics fields.
    home_possession = models.PositiveIntegerField(blank=True, null=True)
    away_possession = models.PositiveIntegerField(blank=True, null=True)
    home_shots = models.PositiveIntegerField(blank=True, null=True)
    away_shots = models.PositiveIntegerField(blank=True, null=True)
    home_on_target = models.PositiveIntegerField(blank=True, null=True)
    away_on_target = models.PositiveIntegerField(blank=True, null=True)
    home_corners = models.PositiveIntegerField(blank=True, null=True)
    away_corners = models.PositiveIntegerField(blank=True, null=True)
    home_fouls = models.PositiveIntegerField(blank=True, null=True)
    away_fouls = models.PositiveIntegerField(blank=True, null=True)
    home_yellow = models.PositiveIntegerField(blank=True, null=True)
    away_yellow = models.PositiveIntegerField(blank=True, null=True)
    home_red = models.PositiveIntegerField(blank=True, null=True)
    away_red = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.home_team.full_name + " v " + self.away_team.full_name + ": " + str(self.game_date)


# Team line-up model for individual games.
class LineUp(models.Model):
    objects = models.Manager()
    game = models.ForeignKey(Game, related_name='lineups', on_delete=models.CASCADE)
    club = models.ForeignKey(Club, related_name='lineup', on_delete=models.CASCADE)
    starter_1 = models.ForeignKey(Player, related_name='starter1name', on_delete=models.CASCADE)
    starter_2 = models.ForeignKey(Player, related_name='starter2name', on_delete=models.CASCADE)
    starter_3 = models.ForeignKey(Player, related_name='starter3name', on_delete=models.CASCADE)
    starter_4 = models.ForeignKey(Player, related_name='starter4name', on_delete=models.CASCADE)
    starter_5 = models.ForeignKey(Player, related_name='starter5name', on_delete=models.CASCADE)
    starter_6 = models.ForeignKey(Player, related_name='starter6name', on_delete=models.CASCADE)
    starter_7 = models.ForeignKey(Player, related_name='starter7name', on_delete=models.CASCADE)
    starter_8 = models.ForeignKey(Player, related_name='starter8name', on_delete=models.CASCADE)
    starter_9 = models.ForeignKey(Player, related_name='starter9name', on_delete=models.CASCADE)
    starter_10 = models.ForeignKey(Player, related_name='starter10name', on_delete=models.CASCADE)
    starter_11 = models.ForeignKey(Player, related_name='starter11name', on_delete=models.CASCADE)
    substitute_1 = models.ForeignKey(Player, related_name='sub1name', on_delete=models.CASCADE)
    substitute_2 = models.ForeignKey(Player, related_name='sub2name', on_delete=models.CASCADE)
    substitute_3 = models.ForeignKey(Player, related_name='sub3name', on_delete=models.CASCADE)
    substitute_4 = models.ForeignKey(Player, related_name='sub4name', on_delete=models.CASCADE)
    substitute_5 = models.ForeignKey(Player, related_name='sub5name', on_delete=models.CASCADE)
    substitute_6 = models.ForeignKey(Player, related_name='sub6name', on_delete=models.CASCADE)
    substitute_7 = models.ForeignKey(Player, related_name='sub7name', on_delete=models.CASCADE)
    substitute_8 = models.ForeignKey(Player, related_name='sub8name', on_delete=models.CASCADE)
    substitute_9 = models.ForeignKey(Player, related_name='sub9name', on_delete=models.CASCADE)
    substitute_10 = models.ForeignKey(Player, related_name='sub10name', on_delete=models.CASCADE)
    substitute_11 = models.ForeignKey(Player, related_name='sub11name', on_delete=models.CASCADE)
    substitute_12 = models.ForeignKey(Player, related_name='sub12name', on_delete=models.CASCADE)

    def __str__(self):
        return self.club.full_name + ": " + self.game.game_date