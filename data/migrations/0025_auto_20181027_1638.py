# Generated by Django 2.1.2 on 2018-10-27 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0024_auto_20181027_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 27, 16, 38, 55, 858127)),
        ),
    ]