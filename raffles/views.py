from django.shortcuts import render

def entry(request, *args, **kwargs):
    return render(request, template_name='raffles/entry.html')

def register(request, *args, **kwargs):
    return render(request, template_name='raffles/register.html')


