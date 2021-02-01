from rest_framework import serializers

from apps.jobs.models import VacancyType, VacancyStatus, Vacancy


class VacancyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyType
        fields = ['title']


class VacancyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyStatus
        fields = ['title']


class VacancySerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()

    class Meta:
        model = Vacancy
        fields = [
            'title',
            'salary',
            'location',
            'description',
            'company',
            'type',
            'status',
            'category',
            'tags',
        ]
