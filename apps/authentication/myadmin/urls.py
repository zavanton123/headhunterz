from django.urls import path

from apps.authentication.myadmin.views import home

app_name = 'authentication_admin'

urlpatterns = [
    path('', home, name='home')
]
