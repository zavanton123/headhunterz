from rest_framework import serializers

from apps.jobs.models import VacancyType, VacancyStatus, Vacancy
from apps.profiles.models import CompanyProfile
from apps.taxonomies.serializers import CategorySerializer


class VacancyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyType
        fields = ['title']


class VacancyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyStatus
        fields = ['title']


class VacancySerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=CompanyProfile.objects.all(),
        source='company',
    )
    company_slug = serializers.SlugRelatedField(
        queryset=CompanyProfile.objects.all(),
        slug_field='slug',
        source='company',
    )
    type_name = serializers.StringRelatedField(
        source='type',
    )
    type_slug = serializers.SlugRelatedField(
        queryset=VacancyType.objects.all(),
        slug_field='slug',
        source='type',
    )
    status_name = serializers.StringRelatedField(
        source='status',
    )
    category = CategorySerializer()

    class Meta:
        model = Vacancy
        fields = [
            'id',
            'title',
            'salary',
            'location',
            'description',
            'company_id',
            'company_slug',
            'type_name',
            'type_slug',
            'status_name',
            'category',
            'tags',
        ]
