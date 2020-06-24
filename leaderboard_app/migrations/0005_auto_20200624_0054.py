# Generated by Django 3.0.7 on 2020-06-24 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard_app', '0004_auto_20200623_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='next_player',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leaderboard_app.Player'),
        ),
        migrations.DeleteModel(
            name='UserPoint',
        ),
    ]