from django.contrib import admin
from .models import Profile, FitnessChallenge, FitnessChallengeProgress


admin.site.register(Profile)
admin.site.register(FitnessChallenge)
admin.site.register(FitnessChallengeProgress)
