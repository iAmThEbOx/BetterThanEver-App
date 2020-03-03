# Generated by Django 2.2 on 2020-02-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200222_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='challenges_completed',
            field=models.ManyToManyField(null=True, to='users.FitnessChallenge'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sleep_end',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sleep_time',
            field=models.TimeField(null=True),
        ),
    ]