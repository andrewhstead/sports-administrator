# Generated by Django 2.1.2 on 2018-10-27 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0023_competition_date_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='date_modified',
            field=models.DateField(default=datetime.datetime(2018, 10, 27, 16, 32, 56, 235143)),
        ),
    ]
