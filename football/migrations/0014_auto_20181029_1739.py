# Generated by Django 2.1.2 on 2018-10-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0013_auto_20181029_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
