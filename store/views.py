from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import StoreItem, StoreItemReview
from users import models as user_models
from django.views import View

class Home(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            login(request, User.objects.filter(username='demouser1234')[0])
        return render(request, template_name='store/home.html')

def landing(request, *args, **kwargs):
    return render(request, template_name='store/landing.html')
            

def store(request, *args, **kwargs):
    return render(request, template_name='store/store.html',
        context={
            'items': StoreItem.objects.all(),
            'balance': request.user.profile.balance,
        }
    )
            
def pricing(request, *args, **kwargs):
    return render(request, template_name='store/pricing.html')
    
