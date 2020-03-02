from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class StoreItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, max_length=500)
    featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='store_pics')
    DEPARTMENT_CHOICES = [
        ('S', 'Shoes'),
        ('C', 'Clothing'),
        ('T', 'Technology'),
    ]
    department = models.CharField(
        max_length=1,
        choices=DEPARTMENT_CHOICES
    )

class StoreItemReview(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Star'),
        (3, '3 Star'),
        (4, '4 Star'),
        (5, '5 Star'),
    ]

    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        choices=RATING_CHOICES
    )

    review = models.TextField(blank=True, default='', max_length=280)

    store_item = models.ForeignKey(StoreItem, on_delete=models.CASCADE)

