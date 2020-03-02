from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login

from .models import Profile, PastWeight, PastHeight
from .forms import (
    UserCreationForm,
    ProfileUpdateForm,
    WeightUpdateForm,
    HeightUpdateForm,
)

from datetime import datetime

class LeaderBoardView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        user_len = len(Profile.objects.all())
        profiles = list(Profile.objects.order_by('-revenue', '-balance'))
        users = [p.user for p in profiles]
        if user_len > 5:
            top = profiles[:7]
        else:
            top = profiles

        context['top'] = top
        if request.user.is_authenticated:
            user_place = users.index(request.user) + 1
            context['user_place'] = user_place
            context['user'] = self.request.user
            if user_place <= 5 and user_place != -1:
                context['user_in_top'] = True
            else:
                context['user_in_top'] = False
        

        return render(request, 'users/leaderboard.html', context)


def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password1=form.cleaned_data['password1'],
                password2=form.cleaned_data['password2']
            )
            login(request, new_user)
            return redirect('profileupdate')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'r_form': form})

class UpdateProfileView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        p_form = ProfileUpdateForm(
            data,
            instance=request.user.profile
        )
        if p_form.is_valid():
            p_form.save()
            return redirect('dashboard')

        return render(request, 'users/profileupdate.html', { 'form': p_form })

    def get(self, request, *args, **kwargs):
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
        return render(request, 'users/profileupdate.html', { 'form': p_form })

class WeightUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = request.POST
            p = request.user.profile
            form = WeightUpdateForm(
                data,
                instance=p,
            )
            if form.is_valid():
                w = PastWeight(
                    profile=p,
                    weight=data['weight'],
                )
                w.save()
                form.save()
                return redirect('dashboard')
        
        else:
            form = WeightUpdateForm(instance=request.user.profile)
        
        return render(request, 'users/weightupdate.html', { 'form': form })

class HeightUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = request.POST
            p = request.user.profile
            form = HeightUpdateForm(
                data,
                instance=p
            )
            if form.is_valid():
                w = PastHeight(
                    profile=p,
                    height=data['height']
                )
                w.save()
                form.save()
                return redirect('dashboard')
        else:
            form = HeightUpdateForm(instance=request.user.profile)
        return render(request, 'users/heightupdate.html', {'form': form})
            
                