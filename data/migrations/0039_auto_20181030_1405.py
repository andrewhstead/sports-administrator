# Generated by Django 2.1.2 on 2018-10-30 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0038_auto_20181030_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 30, 14, 5, 10, 450323)),
        ),
    ]
