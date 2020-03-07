"""better_than_ever URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from store import views as store_views
from django.contrib.auth import views as auth_views

# Registration and login currently broken 03-01-20

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leaderboard/', user_views.LeaderBoardView.as_view(), name='leaderboard'),
    path('weightupdate/', user_views.WeightUpdateView.as_view(), name='weightupdate'),
    path('profileupdate/', user_views.UpdateProfileView.as_view(), name='profileupdate'),
    path('signup/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/register.html'), name='login'),
    path('store/', store_views.store, name='store'),
    path('workouts/', include('workouts.urls')),
    path('recipes/', include('recipes.urls')),
    path('generalhealth/', include('general_health.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Test users have their password in the form Password!{Number}