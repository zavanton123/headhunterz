from django.urls import path

from apps.profiles.views import demo

app_name = 'profiles'

urlpatterns = [
    path('', demo, name='demo'),
]
