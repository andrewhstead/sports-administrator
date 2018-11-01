# Generated by Django 2.1.2 on 2018-11-01 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0042_auto_20181101_1732'),
        ('football', '0024_auto_20181101_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaguerecord',
            name='season',
        ),
        migrations.AddField(
            model_name='clubseason',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club', to='data.Season'),
        ),
    ]
