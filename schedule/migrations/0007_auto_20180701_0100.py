# Generated by Django 2.0.5 on 2018-06-30 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_auto_20180630_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulepost',
            name='image',
            field=models.ImageField(upload_to='schedule/%Y/%m/%d'),
        ),
    ]