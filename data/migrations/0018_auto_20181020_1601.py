# Generated by Django 2.1.2 on 2018-10-20 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0017_competition_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='type',
            field=models.CharField(choices=[('league', 'League Competition'), ('knockout', 'Knockout Competition')], max_length=10),
        ),
    ]
