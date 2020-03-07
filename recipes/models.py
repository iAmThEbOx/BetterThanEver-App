from django.db import models



# Create your models here.
class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('FR', 'Fruit'),
        ('VE', 'Vegetables'),
        ('ME', 'Meat'),
        ('GR', 'Grains'),
        ('CA', 'Carbs'),
        ('DE', 'Dessert'),
    ]
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140)
    category = models.CharField(
        max_length=2, choices=CATEGORY_CHOICES
    )
    link = models.URLField()
    cooking_time = models.CharField(max_length=30)
    image = models.ImageField(upload_to='recipe_pics', default='escher_pic.jpg')

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

class RecipeInfo(models.Model):
    prep_time = models.CharField(max_length=140)
    active_time = models.CharField(max_length=140)
    cook_time = models.CharField(max_length=140)
    nutrition_info = models.OneToOneField(NutritionInfo, on_delete=models.CASCADE)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)



