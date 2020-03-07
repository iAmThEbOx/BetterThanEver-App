from django.shortcuts import render

def general_health(request, *args, **kwargs):
    return render(
        request,
        template_name='general_health/general_health.html',
        context={'user': request.user}
    )

def landing(request, *args, **kwargs):
    return render(request, template_name='general_health/mental_health_landing.html')

def evaluation(request, *args, **kwargs):
    return render(request, template_name='general_health/evaluation.html')

def sleep_timer(request, *args, **kwargs):
    return render(request, template_name='general_health/timer.html')