# Generated by Django 3.0.4 on 2020-03-07 00:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20200304_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnesschallengeprogress',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 8, 0, 41, 32, 443159)),
        ),
    ]
