from rest_framework import serializers

from apps.jobs.models import VacancyType, VacancyStatus, Vacancy
from apps.profiles.models import PersonProfile
from apps.profiles.serializers import CompanySerializer
from apps.taxonomies.serializers import CategorySerializer, TagSerializer


class VacancyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyType
        fields = ['title']


class VacancyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyStatus
        fields = ['title']


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    candidates = serializers.PrimaryKeyRelatedField(
        queryset=PersonProfile.objects.all(),
        many=True,
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
    tags = TagSerializer(many=True)

    class Meta:
        model = Vacancy
        fields = [
            'id',
            'title',
            'salary',
            'location',
            'description',
            'company',
            'candidates',
            'type_slug',
            'status_name',
            'category',
            'tags',
        ]
