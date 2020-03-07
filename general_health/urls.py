from django.urls import path
from .views import general_health, landing, evaluation, sleep_timer 

urlpatterns = [
    path('', general_health, name='general_health'),
    path('landing', landing, name='general_health_landing'),
    path('evaluate', evaluation, name='general_health_evaluation'),
    path('timer', sleep_timer, name='sleep_timer'),
]