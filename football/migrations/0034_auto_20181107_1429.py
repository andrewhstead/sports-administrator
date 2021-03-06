# Generated by Django 2.1.2 on 2018-11-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0033_game_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='attendance',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='away_corners',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='away_fouls',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='away_on_target',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='away_possession',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='away_red',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='away_score',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='away_shots',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='away_yellow',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_corners',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_fouls',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_on_target',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_possession',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_red',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_score',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_shots',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_yellow',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='away_against',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='away_drawn',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='away_for',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='away_lost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='away_played',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='away_won',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='home_against',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='home_drawn',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='home_for',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='home_lost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='home_played',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='home_won',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='position',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='total_against',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='total_drawn',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='total_for',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='total_lost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='total_played',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='total_points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leaguerecord',
            name='total_won',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
