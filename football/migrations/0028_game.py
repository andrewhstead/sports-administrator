# Generated by Django 2.1.2 on 2018-11-05 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0027_leaguerecord_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed')], default='Scheduled', max_length=10)),
                ('game_date', models.DateField()),
                ('game_time', models.TimeField(blank=True, null=True)),
                ('neutral_venue', models.BooleanField(default=False)),
                ('home_score', models.IntegerField(blank=True, null=True)),
                ('away_score', models.IntegerField(blank=True, null=True)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_away', to='football.Club')),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='football.Edition')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_home', to='football.Club')),
            ],
        ),
    ]