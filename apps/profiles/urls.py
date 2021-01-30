from django.urls import path

from apps.profiles.views import demo, ShowPersonsProfiles

app_name = 'profiles'

urlpatterns = [
    path('', demo, name='demo'),
    path('persons/', ShowPersonsProfiles.as_view(), name='all_persons'),
]
