# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Sport, Country, Competition, Season, Edition

# Register your models here.
admin.site.register(Sport)
admin.site.register(Country)
admin.site.register(Competition)
admin.site.register(Season)
admin.site.register(Edition)