from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'height',
            'weight',
            'date_of_birth',
            'gender',
            'sleep_time',
            'sleep_end',
            'balance',
            'address',
            'phone_number',
        )

        