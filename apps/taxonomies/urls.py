from django.urls import path

from apps.taxonomies.views import home

app_name = 'taxonomies'

urlpatterns = [
    path('', home, name='home'),
]
