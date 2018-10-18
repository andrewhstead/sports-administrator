from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Options for different types of site, to determine which modules are available.
SITE_OPTIONS = (
    ('individual', "Individual Player"),
    ('club', "Single Club"),
    ('competition', "Single Competition"),
    ('multi', "Multiple Competitions"),
)


# Create your models here.
# Additional fields are added to the AbstractUser model.
class User(AbstractUser):
    objects = UserManager()
    organisation = models.CharField(max_length=50, blank=True, null=True)
    site_name = models.CharField(max_length=50, blank=True, null=True)
    site_type = models.CharField(max_length=25, choices=SITE_OPTIONS, blank=True, null=True)
    primary_color = models.CharField(max_length=10, blank=True, null=True, default="#ffffff")
    secondary_color = models.CharField(max_length=10, blank=True, null=True, default="#ffffff")
    primary_text = models.CharField(max_length=10, blank=True, null=True, default="#000000")
    secondary_text = models.CharField(max_length=10, blank=True, null=True, default="#000000")

    def __unicode__(self):
        return self.username