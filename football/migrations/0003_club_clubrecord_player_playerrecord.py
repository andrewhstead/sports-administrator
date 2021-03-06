# Generated by Django 2.1.2 on 2018-10-24 16:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_competition'),
        ('football', '0002_auto_20181024_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, unique=True)),
                ('short_name', models.CharField(max_length=15, unique=True)),
                ('abbreviation', models.CharField(max_length=3, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clubs', to='data.Country')),
            ],
        ),
        migrations.CreateModel(
            name='ClubRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=15)),
                ('abbreviation', models.CharField(max_length=3)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_years', to='football.Club')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club', to='data.Season', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('middle_names', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('current_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_players', to='football.Club')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='football.Club')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_years', to='football.Player')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='data.Season')),
            ],
        ),
    ]
