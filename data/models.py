from __future__ import unicode_literals
from django.db import models

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
        
        
class Competition(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, related_name='competitions', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='competitions', on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name