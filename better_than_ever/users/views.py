from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Profile

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