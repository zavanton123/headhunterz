from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.profiles.models import PersonProfile
from apps.profiles.serializers import PersonProfileSerializer, CreatePersonSerializer


class PersonsApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        persons = PersonProfile.objects.all()
        serializer = PersonProfileSerializer(instance=persons, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CreatePersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        result = {
            'result': 'success',
        }
        return Response(data=result, status=status.HTTP_201_CREATED)
