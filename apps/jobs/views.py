from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.authentication.permissions import IsSuperUserOrReadOnly
from apps.jobs.models import VacancyType
from apps.jobs.serializers import VacancyTypeSerializer


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
