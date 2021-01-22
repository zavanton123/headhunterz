from django.urls import path

from apps.authentication.views import register

app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
]
