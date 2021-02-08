from django.urls import path, include

app_name = 'authentication'

urlpatterns = [
    # djoser authentication endpoints
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
