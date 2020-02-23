from django.contrib import admin
from .models import (
    Recipe,
    RecipeInfo,
    RecipeIngredient,
    RecipeStep,
    NutritionInfo
)

admin.site.register(Recipe)
admin.site.register(RecipeInfo)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeStep)
admin.site.register(NutritionInfo)
