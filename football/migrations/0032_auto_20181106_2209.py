# Generated by Django 2.1.2 on 2018-11-06 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0031_game_date_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
