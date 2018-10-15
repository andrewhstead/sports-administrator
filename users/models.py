from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
# Additional fields are added to the AbstractUser model.
class User(AbstractUser):
    objects = UserManager()
    organisation = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.username