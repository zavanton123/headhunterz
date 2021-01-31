from django.urls import path, include
from rest_framework import routers

from apps.jobs.views import VacancyTypeViewSet

app_name = 'jobs'

router = routers.DefaultRouter()
router.register(r'types', VacancyTypeViewSet, basename='vacancy-types')

urlpatterns = [
    path('vacancies/', include(router.urls)),
]
