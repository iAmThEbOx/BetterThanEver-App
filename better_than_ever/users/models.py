from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    balance = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=14, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class FitnessChallengeProgress(models.Model):
    pass

class FitnessChallenge(models.Model):
    pass
