# Generated by Django 2.1.2 on 2018-11-08 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0051_auto_20181107_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 8, 17, 28, 15, 441143)),
        ),
    ]
