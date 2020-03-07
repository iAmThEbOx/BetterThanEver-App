from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import StoreItem, StoreItemReview
from users import models as user_models
from django.views import View

class Home(View):
    def get(self, request, *args, **kwargs):
        context = {}
        if request.user.is_authenticated:
            context['user'] = request.user
            context['past_weights'] = user_models.PastWeight.objects.filter(profile=request.user.profile)
            context['past_heights'] = user_models.PastHeight.objects.filter(profile=request.user.profile)

def store(request, *args, **kwargs):
    return render(request, template_name='store/store.html',
        context={
            'items': StoreItem.objects.all(),
            'balance': request.user.profile.balance,
        }
    )
            
    
