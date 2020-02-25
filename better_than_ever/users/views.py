from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login

from .models import Profile
from .forms import UserCreationForm, ProfileUpdateForm

class LeaderBoardView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        user_len = len(Profile.objects.all())
        profiles = list(Profile.objects.order_by('-revenue', '-balance'))
        users = [p.user for p in profiles]
        if user_len > 5:
            top = profiles[:6]
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

class RegisterUserView(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                new_user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                )
                login(request, new_user)
                return HttpResponseRedirect('profileupdate')
        else:
            form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})

class UpdateProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = request.POST
            data['user'] = request.user
            p_form = ProfileUpdateForm(
                data,
                instance=request.user.profile
            )
            if p_form.is_valid():
                p_form.save()
                return HttpResponseRedirect('dashboard')
        
        else:
            p_form = ProfileUpdateForm(instance=request.user.profile)
        
        return render(request, 'users/profileupdate.html', {'form': p_form})

            
                