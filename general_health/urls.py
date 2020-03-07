from django.urls import path
from .views import general_health

urlpatterns = [
    path('', general_health, name='general_health')
]