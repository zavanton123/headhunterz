from django.urls import path

from apps.jobs.views import job_demo

app_name = 'jobs'

urlpatterns = [
    path('', job_demo, name='jobdemo'),
]
