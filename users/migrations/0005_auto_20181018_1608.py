# Generated by Django 2.1.2 on 2018-10-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20181017_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='primary_color',
            field=models.CharField(blank=True, default='#ffffff', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='primary_text',
            field=models.CharField(blank=True, default='#000000', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='secondary_color',
            field=models.CharField(blank=True, default='#ffffff', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='secondary_text',
            field=models.CharField(blank=True, default='#000000', max_length=10, null=True),
        ),
    ]
