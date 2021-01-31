from django.urls import path

from apps.profiles.views import ShowPersonsProfiles

app_name = 'profiles'

urlpatterns = [
    path('persons/', ShowPersonsProfiles.as_view(), name='all_persons'),
]
