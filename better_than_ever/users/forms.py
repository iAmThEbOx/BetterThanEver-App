from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['height', 'weight', 'date_of_birth', 'gender', 'address', 'phone_number', 'revenue']

class SleepUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['sleep_time', 'sleep_end']

class WeightHeightUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['weight', 'height']

        