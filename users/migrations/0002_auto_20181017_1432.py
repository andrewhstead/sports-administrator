# Generated by Django 2.1.2 on 2018-10-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='site_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='size',
            field=models.CharField(blank=True, choices=[('individual', 'Individual Player'), ('club', 'Single Club'), ('competition', 'Single Competition'), ('multi', 'Multiple Competitions')], max_length=25, null=True),
        ),
    ]