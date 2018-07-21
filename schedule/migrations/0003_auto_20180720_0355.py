# Generated by Django 2.0.5 on 2018-07-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20180716_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulepost',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='schedulepost',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='schedulepost',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]