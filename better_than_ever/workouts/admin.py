from django.contrib import admin
from .models import (
    Bodyweight,
    Cardio,
    StrengthTraining,
    Flexibility,
    Meditation,
    SpeedAndAgility
)

admin.site.register(Bodyweight)
admin.site.register(Cardio)
admin.site.register(StrengthTraining)
admin.site.register(Flexibility)
admin.site.register(Meditation)
admin.site.register(SpeedAndAgility)
