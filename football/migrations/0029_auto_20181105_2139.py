# Generated by Django 2.1.2 on 2018-11-05 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0028_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='edition',
            name='away_draw_points',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='edition',
            name='away_loss_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='edition',
            name='away_win_points',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='edition',
            name='bottom_primary_places',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='edition',
            name='bottom_secondary_places',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='edition',
            name='home_draw_points',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='edition',
            name='home_loss_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='edition',
            name='home_win_points',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='edition',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='edition',
            name='tie_breaker_1',
            field=models.CharField(choices=[('Goal Average', 'Goal Average'), ('Goal Difference', 'Goal Difference'), ('Goals For', 'Goals For'), ('Games Won', 'Games Won'), ('Name', 'Name')], default='Name', max_length=25),
        ),
        migrations.AddField(
            model_name='edition',
            name='tie_breaker_2',
            field=models.CharField(choices=[('Goal Average', 'Goal Average'), ('Goal Difference', 'Goal Difference'), ('Goals For', 'Goals For'), ('Games Won', 'Games Won'), ('Name', 'Name')], default='Name', max_length=25),
        ),
        migrations.AddField(
            model_name='edition',
            name='tie_breaker_3',
            field=models.CharField(choices=[('Goal Average', 'Goal Average'), ('Goal Difference', 'Goal Difference'), ('Goals For', 'Goals For'), ('Games Won', 'Games Won'), ('Name', 'Name')], default='Name', max_length=25),
        ),
        migrations.AddField(
            model_name='edition',
            name='tie_breaker_4',
            field=models.CharField(choices=[('Goal Average', 'Goal Average'), ('Goal Difference', 'Goal Difference'), ('Goals For', 'Goals For'), ('Games Won', 'Games Won'), ('Name', 'Name')], default='Name', max_length=25),
        ),
        migrations.AddField(
            model_name='edition',
            name='tie_breaker_5',
            field=models.CharField(choices=[('Goal Average', 'Goal Average'), ('Goal Difference', 'Goal Difference'), ('Goals For', 'Goals For'), ('Games Won', 'Games Won'), ('Name', 'Name')], default='Name', max_length=25),
        ),
        migrations.AddField(
            model_name='edition',
            name='top_primary_places',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='edition',
            name='top_secondary_places',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
