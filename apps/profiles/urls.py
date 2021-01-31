from django.urls import path

from apps.profiles.views import PersonsApiView

app_name = 'profiles'

urlpatterns = [
    path('persons/', PersonsApiView.as_view()),
]
