from django.db import models

class Food(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=500)
    prep_time = models.CharField(max_length=50)

# Create your models here.
class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('FR', 'Fruits'),
        ('VE', 'Vegetables'),
        ('ME', 'Meats'),
        ('GR', 'Grains'),
        ('CA', 'Carbohydrates'),
        ('DE', 'Desserts')
    ]
    category = models.CharField(
        max_length=2, choices=CATEGORY_CHOICES
    )

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=140)

class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step = models.CharField(max_length=140)

class NutritionInfo(models.Model):
    servings_per = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()
    added_sugars = models.PositiveIntegerField()

class RecipeInfo(models.Model)
    active_time = models.CharField(max_length=140)
    nutrition_info = models.OneToOneField(NutritionInfo, on_delete=models.CASCADE)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)



