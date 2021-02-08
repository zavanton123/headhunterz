import logging

from rest_framework import permissions, status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.profiles.models import PersonProfile, CompanyProfile
from apps.profiles.serializers import PersonSerializer, CreatePersonSerializer, CreateCompanySerializer, \
    CompanySerializer, UpdatePersonSerializer

log = logging.getLogger(__name__)


class PersonsApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        persons = PersonProfile.objects.all()
        serializer = PersonSerializer(instance=persons, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CreatePersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        result = {
            'result': 'created',
        }
        return Response(data=result, status=status.HTTP_201_CREATED)


class PersonApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonProfile.objects.all()
    serializer_class = CreatePersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CreatePersonSerializer
        return PersonSerializer

    def update(self, request, pk, *args, **kwargs):
        person = get_object_or_404(PersonProfile, pk=pk)
        serializer = UpdatePersonSerializer(instance=person, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        result = {
            'result': 'person profile info is updated'
        }
        return Response(data=result, status=status.HTTP_204_NO_CONTENT)


class CompaniesApiView(generics.ListCreateAPIView):
    queryset = CompanyProfile.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateCompanySerializer
        return CompanySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = {
            'result': 'created'
        }
        return Response(
            data=data,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(response.data)
        )


class CompanyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyProfile.objects.all()
    permission_classes = [permissions.AllowAny]  # todo zavanton -

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CreateCompanySerializer
        return CompanySerializer
