# Generated by Django 2.1.2 on 2018-10-19 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_auto_20181019_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editions', to='data.Season', unique=True),
        ),
    ]