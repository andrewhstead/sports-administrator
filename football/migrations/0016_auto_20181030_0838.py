# Generated by Django 2.1.2 on 2018-10-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0015_auto_20181029_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubrecord',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='clubrecord',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clubrecord',
            name='short_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
