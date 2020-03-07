from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Workout
# #
def general(request, *args, **kwargs):
    if request.method == 'GET':
        context = {
            'workouts': Workout.objects.filter(category='GE')
        }
        return render(request, 'workouts/general.html', context)

def cardio(request, *args, **kwargs):
    if request.method == 'GET':
        context = {
            'workouts': Workout.objects.filter(category='CA')
        }
        return render(request, 'workouts/cardio.html', context)

def strength(request, *args, **kwargs):
    if request.method == 'GET':
        context = {
            'workouts': Workout.objects.filter(category='ST')
        }
        return render(request, 'workouts/strength.html', context)

def flexibility(request, *args, **kwargs):
    if request.method == 'GET':
        context = {
            'workouts': Workout.objects.filter(category='FL')
        }
        return render(request, 'workouts/flexibility.html', context)

def meditation(request, *args, **kwargs):
    if request.method == 'GET':
        context = {
            'workouts': Workout.objects.filter(category='ME')
        }
        return render(request, 'workouts/meditation.html', context)

def speed(request, *args, **kwargs):
    if request.method == 'GET':
        context = {
            'workouts': Workout.objects.filter(category='SP')
        }
        return render(request, 'workouts/speed.html', context)

def catalog(request, *args, **kwargs):
    return render(request, template_name='workouts/catalog.html')


