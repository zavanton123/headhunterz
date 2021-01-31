from django.urls import path

from apps.profiles.views import PersonsApiView, CompaniesApiView, CompanyApiView, PersonApiView

app_name = 'profiles'

urlpatterns = [
    path('persons/', PersonsApiView.as_view()),
    path('persons/<int:pk>/', PersonApiView.as_view()),
    path('companies/', CompaniesApiView.as_view()),
    path('companies/<int:pk>/', CompanyApiView.as_view()),
]
