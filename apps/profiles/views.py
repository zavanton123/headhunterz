from rest_framework import generics

from apps.profiles.models import PersonProfile
from apps.profiles.serializers import PersonProfileSerializer


class ShowPersonsProfiles(generics.ListAPIView):
    queryset = PersonProfile.objects.all()
    serializer_class = PersonProfileSerializer
