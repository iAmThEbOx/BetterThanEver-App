# Generated by Django 2.2 on 2020-02-24 23:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200224_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnesschallengeprogress',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 25, 23, 46, 12, 508638)),
        ),
    ]
