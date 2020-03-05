from django.urls import path
from .views import (
    cardio,
    general,
    flexibility,
    meditation,
    speed,
    strength,
)

urlpatterns = [
    path('general', general, name='workouts-general'),
    path('cardio', cardio, name='workouts-cardio'),
    path('flexibility', flexibility, name='workouts-flexibility'),
    path('meditation', meditation, name='workouts-meditation'),
    path('speed', speed, name='workouts-speed'),
    path('strength', general, name='workouts-strength'),
]