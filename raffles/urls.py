from django.urls import path
from .views import (
    entry,
    register,
)

urlpatterns = [
    path('', entry, name='entry'),
    path('register', register, name='raffle-register'),
]