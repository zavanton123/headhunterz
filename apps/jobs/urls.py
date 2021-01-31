from django.urls import path, include
from rest_framework import routers

from apps.jobs.views import VacancyTypeViewSet, VacancyStatusViewSet

app_name = 'jobs'

router = routers.DefaultRouter()
router.register(r'types', VacancyTypeViewSet, basename='vacancy-types')
router.register(r'statuses', VacancyStatusViewSet, basename='vacancy-statuses')

urlpatterns = [
    path('vacancies/', include(router.urls)),
]
