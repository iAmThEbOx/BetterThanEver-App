from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.validators import MinValueValidator, MaxValueValidator

class CustomUser(AbstractUser):
    height = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(120)]
    )
    weight = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(2), MaxValueValidator(1500)]
    )
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(150)]
    )
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )
    profile_pic = models.ImageField(height_field=200, width_field=200)
    sleep_time = models.TimeField()
    sleep_end = models.TimeField()
    balance = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    challenges_completed = models.ManyToManyField('FitnessChallenge', on_delete=models.CASCADE)



