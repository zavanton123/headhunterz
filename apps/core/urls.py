from django.urls import path

from apps.core.views import favicon_placeholder

app_name = 'core'

urlpatterns = [
    path('favicon.ico/', favicon_placeholder, name='favicon_placeholder')
]
