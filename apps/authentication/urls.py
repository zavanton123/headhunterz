from django.urls import path, include

from apps.authentication.views import register

app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),

    # djoser authentication endpoints
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),  # optional
    # path('', include('djoser.urls.authtoken')),  # optional
    # path('', include('djoser.social.urls')),  # optional
]
