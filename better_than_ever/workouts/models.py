from django.db import models

class Workout(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=500)
    INTENSITY_CHOICES= [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High')
    ]
    intensity = models.CharField(max_length=1, choices=INTENSITY_CHOICES)
    CATEGORY_CHOICES = [
        ('CA', 'Cardio'),
        ('ST', 'Strength'),
        ('EN', 'Endurance'),
        ('FL', 'Flexibility'),
        ('ME', 'Meditation'),
        ('SP', 'Speed')
    ]
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.title}'

