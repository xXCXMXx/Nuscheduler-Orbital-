# Generated by Django 2.0.5 on 2018-07-20 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_schedulepost_upvoted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedulepost',
            old_name='upvoted',
            new_name='like',
        ),
    ]
