from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.profiles.models import PersonProfile
from apps.profiles.serializers import PersonProfileSerializer


@api_view(http_method_names=['GET'])
def demo(request):
    return Response({'demo': "demo"})


class ShowPersonsProfiles(generics.ListAPIView):
    queryset = PersonProfile.objects.all()
    serializer_class = PersonProfileSerializer
