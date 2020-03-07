from django.urls import path
from .views import (
    cardio,
    general,
    flexibility,
    meditation,
    speed,
    strength,
    catalog,
)

urlpatterns = [
    path('general', general, name='workouts-general'),
    path('cardio', cardio, name='workouts-cardio'),
    path('flexibility', flexibility, name='workouts-flexibility'),
    path('meditation', meditation, name='workouts-meditation'),
    path('speed', speed, name='workouts-speed'),
    path('strength', strength, name='workouts-strength'),
    path('', catalog, name='workouts-catalog'),
]