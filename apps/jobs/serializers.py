from rest_framework import serializers

from apps.jobs.models import VacancyType


class VacancyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyType
        fields = ['title']
