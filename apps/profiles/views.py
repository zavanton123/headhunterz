from rest_framework import permissions, status, generics
from rest_framework.response import Response

from apps.profiles.models import PersonProfile
from apps.profiles.serializers import PersonProfileSerializer


class PersonsApiView(generics.GenericAPIView):
    queryset = PersonProfile.objects.all()
    serializer_class = PersonProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        persons = self.get_queryset()
        serializer = self.serializer_class(instance=persons, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
