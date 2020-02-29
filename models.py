from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Workouts(models.Model):
    CATEGORY_CHOICES = [
        ('ES','estimated time'),
        ('TT','title'),
        ('DS','description'),
        ('WC','category')
    ]
    category = models.CharField(
        max_length=2, choices=CATEGORY_CHOICES
    )
# user will click on the description the user will be redirected to the source URL (where the workouts are found from)

class Bodyweight(models.Model):
    # let's add the exercises scraped from a collective archive
    title = models.CharField(max_length=100)
    exercise = models.ForeignKey(exercise,on_delete=models.CASCADE)
    workout_description = models.TextField(blank=True, max_length=500)
    workout_link = models.URLField(maxlength=240)
    
class StrengthTraining(models.Model):
    # parse URLs from youtube
    title = models.CharField(max_length=100)
    exercise = models.ForeignKey(exercise,on_delete=models.CASCADE)
    workout_description = models.TextField(blank=True, max_length=500)
    workout_link = models.URLField(maxlength=240)

class Cardio(models.Model):
    title = models.CharField(max_length=100)
    exercise = models.ForeignKey(exercise,on_delete=models.CASCADE)
    workout_description = models.TextField(blank=True, max_length=500)
    workout_link = models.URLField(maxlength=240)


class SpeedAndAgility(models.Model):
    title = models.CharField(max_length=100)
    exercise = models.ForeignKey(exercise,on_delete=models.CASCADE)
    workout_description = models.TextField(blank=True, max_length=500)
    workout_link = models.URLField(maxlength=240)


class Flexibility(models.Model):
    # range and mobility, stretches (take from book)
    # copy paste the description and title etc from directly the book
    title = models.CharField(max_length=100)
    exercise = models.ForeignKey(exercise,on_delete=models.CASCADE)
    workout_description = models.TextField(blank=True, max_length=500)
    workout_link = models.URLField(maxlength=240)

class Meditation(models.Model):
    title = models.CharField(max_length=100)
    exercise = models.ForeignKey(exercise,on_delete=models.CASCADE)
    workout_description = models.TextField(blank=True, max_length=500)
    workout_link = models.URLField(maxlength=240)
