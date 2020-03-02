from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['height', 'weight', 'date_of_birth', 'gender', 'address', 'phone_number']


class WeightUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['weight']

class HeightUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['height']

        