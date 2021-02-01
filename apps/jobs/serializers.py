from rest_framework import serializers

from apps.jobs.models import VacancyType, VacancyStatus, Vacancy
from apps.profiles.models import CompanyProfile


class VacancyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyType
        fields = ['title']


class VacancyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyStatus
        fields = ['title']


class VacancySerializer(serializers.ModelSerializer):
    company_slug = serializers.SlugRelatedField(
        queryset=CompanyProfile.objects.all(),
        slug_field='slug',
        source='company',
    )
    type_slug = serializers.SlugRelatedField(
        queryset=VacancyType.objects.all(),
        slug_field='slug',
        source='type',
    )

    class Meta:
        model = Vacancy
        fields = [
            'id',
            'title',
            'salary',
            'location',
            'description',
            'company_slug',
            'type_slug',
            'status',
            'category',
            'tags',
        ]
