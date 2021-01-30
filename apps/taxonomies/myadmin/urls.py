from django.urls import path

from apps.taxonomies.myadmin.views import more

app_name = 'taxonomies_admin'

urlpatterns = [
    path('', more, name='more'),
]
