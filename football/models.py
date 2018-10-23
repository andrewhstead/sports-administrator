from django.db import models
from data.models import Sport, Country, Season

# Options for different types of competition.
COMPETITION_TYPES = (
    ('team', "Team Competition"),
    ('individual', "Individual Competition"),
)

# Options for different formats of competition.
COMPETITION_FORMATS = (
    ('league', "League Competition"),
    ('knockout', "Knockout Competition"),
)

# Create your models here.
class Competition(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, related_name='competitions', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='competitions', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=COMPETITION_TYPES)
    format = models.CharField(max_length=10, choices=COMPETITION_FORMATS)
    is_active = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name


class Edition(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    competition = models.ForeignKey(Competition, related_name='editions', on_delete=models.CASCADE)
    season = models.ForeignKey(Season, related_name='editions', on_delete=models.CASCADE, unique=True)
    is_current = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name