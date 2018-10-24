from django.db import models
from data.models import Competition, Season

# Create your models here.
class Edition(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    competition = models.ForeignKey(Competition, related_name='editions', on_delete=models.CASCADE)
    season = models.ForeignKey(Season, related_name='editions', on_delete=models.CASCADE, unique=True)
    is_current = models.BooleanField(default=True)
   
    def __str__(self):
        return self.name