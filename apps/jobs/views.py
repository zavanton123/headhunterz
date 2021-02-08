from rest_framework import viewsets, status, generics, permissions
from rest_framework.response import Response

from apps.authentication.permissions import IsSuperUserOrReadOnly
from apps.jobs.models import VacancyType, VacancyStatus, Vacancy, Application
from apps.jobs.serializers import VacancyTypeSerializer, VacancyStatusSerializer, VacancySerializer, \
    CreateVacancySerializer, CreateApplicationSerializer
from apps.profiles.permissions import IsCompanyProfile, IsPersonProfile


class VacancyTypeViewSet(viewsets.ModelViewSet):
    queryset = VacancyType.objects.all()
    serializer_class = VacancyTypeSerializer
    permission_classes = [IsSuperUserOrReadOnly]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        headers = self.get_success_headers(response.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)


class VacancyStatusViewSet(viewsets.ModelViewSet):
    queryset = VacancyStatus.objects.all()
    serializer_class = VacancyStatusSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class VacancyApiView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | IsCompanyProfile]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateVacancySerializer
        return VacancySerializer


class ApplicationApiView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = CreateApplicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | IsPersonProfile]

    def create(self, request, *args, **kwargs):
        # response = super().create(request, *args, **kwargs)
        # headers = self.get_success_headers(response.data)
        return super().create(request, *args, **kwargs)
