# Generated by Django 2.1.2 on 2018-10-25 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_competition'),
        ('football', '0003_club_clubrecord_player_playerrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='data.Country'),
        ),
        migrations.AddField(
            model_name='player',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='current_club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_players', to='football.Club'),
        ),
        migrations.AlterField(
            model_name='player',
            name='middle_names',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
