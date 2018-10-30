# Generated by Django 2.1.2 on 2018-10-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0019_auto_20181030_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubrecord',
            name='status',
            field=models.CharField(blank=True, choices=[('c', 'Champions'), ('p', 'Promoted'), ('r', 'Relegated'), ('po', 'Play-Offs'), ('ppo', 'Promoted after Play-Offs'), ('rpo', 'Relegated after Play-Offs')], max_length=50, null=True),
        ),
    ]
