# Generated by Django 2.2 on 2020-02-24 23:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200224_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnesschallengeprogress',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 25, 23, 46, 57, 276932)),
        ),
        migrations.CreateModel(
            name='PastSleepHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sleep_start', models.TimeField()),
                ('sleep_end', models.TimeField()),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
    ]
