from django.shortcuts import render

def general_health(request, *args, **kwargs):
    return render(
        request,
        template_name='general_health/general_health.html',
        context={'user': request.user, 'bmi': request.user.profile.weight/(request.user.profile.height**2)}
    )