# Generated by Django 2.1.2 on 2018-11-08 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0035_game_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='edition',
            name='named_substitutes',
            field=models.IntegerField(default=5),
        ),
    ]