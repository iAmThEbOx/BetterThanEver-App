# Generated by Django 2.2 on 2020-02-29 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20200225_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnesschallengeprogress',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 1, 19, 30, 38, 231831)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]