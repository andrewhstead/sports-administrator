from __future__ import unicode_literals
from django.db import models
import datetime
now = datetime.datetime.now()

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

# Options for different types of season, to set as calendar year or multi-year.
SEASON_OPTIONS = (
    ('calendar', "Single Calendar Year"),
    ('multiple', "Span Multiple Years"),
)

# Create your models here.
class Sport(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=25, unique=True)
    icon = models.ImageField(upload_to="images/sports", blank=True, null=True)
   
    def __str__(self):
        return self.name
        
        
class Country(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=25, unique=True)
    abbreviation = models.CharField(max_length=25, unique=True)
    flag = models.ImageField(upload_to="images/countries", blank=True, null=True)
   
    def __str__(self):
        return self.name
        
        
class Season(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=10, choices=SEASON_OPTIONS)
   
    def __str__(self):
        return self.name
        
        
class Competition(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, related_name='competitions', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='competitions', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=COMPETITION_TYPES)
    format = models.CharField(max_length=10, choices=COMPETITION_FORMATS)
    date_modified = models.DateTimeField(default=now)
    is_active = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name
