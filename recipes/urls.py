from django.urls import path
from .views import (
    fruit,
    veg,
    meat,
    grains,
    carbs,
    dessert,
    catalog,
)

urlpatterns = [
    path('', catalog, name='catalog'),
    path('fruit', fruit, name='fruit'),
    path('vegetable', veg, name='vegetable'),
    path('meat', meat, name='meat'),
    path('grains', grains, name='grain'),
    path('carbs', carbs, name='carb'),
    path('dessert', dessert, name='dessert'),
]