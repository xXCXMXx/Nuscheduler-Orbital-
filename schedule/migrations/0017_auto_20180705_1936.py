# Generated by Django 2.0.5 on 2018-07-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0016_auto_20180705_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulepost',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]