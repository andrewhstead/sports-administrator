# Generated by Django 2.1.2 on 2018-10-16 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20181016_0749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sport',
            old_name='sport_name',
            new_name='name',
        ),
    ]