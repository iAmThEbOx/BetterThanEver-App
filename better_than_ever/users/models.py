from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import datetime, timedelta

class Profile(models.Model):
    height = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(120)],
        null=True,
    )
    weight = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(2), MaxValueValidator(1500)],
        null=True,
    )
    date_of_birth = models.DateField(auto_now=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
    )
    sleep_time = models.TimeField(null=True)
    sleep_end = models.TimeField(null=True)
    balance = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=14, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    revenue = models.DecimalField(default=0, max_digits=20, decimal_places=2)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class FitnessChallenge(models.Model):
    challenge_text = models.TextField(max_length=300)
    worth = models.DecimalField(
        default=0, max_digits=20, decimal_places=2
    )
    challenge_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.challenge_text}'


class FitnessChallengeProgress(models.Model):
    fitness_challenge = models.ForeignKey(FitnessChallenge, on_delete=models.CASCADE)
    progress = models.DecimalField(
        max_digits=8, decimal_places=7, default=0
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_accepted = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(
        default=datetime.utcnow() + timedelta(days=1)
    )

    def __str__(self):
        return f'{self.fitness_challenge.challenge_text}: {self.user.username}\'s at {self.progress}'


    

