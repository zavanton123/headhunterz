import logging

from rest_framework import serializers

from apps.jobs.models import VacancyType, VacancyStatus, Vacancy
from apps.profiles.models import PersonProfile
from apps.profiles.serializers import CompanySerializer
from apps.taxonomies.serializers import CategorySerializer, TagSerializer

log = logging.getLogger(__name__)


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
    candidate_count = serializers.SerializerMethodField(method_name='_count_candidates')
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

    def _count_candidates(self, vacancy, *args, **kwargs):
        return len(vacancy.candidates.all())

    class Meta:
        model = Vacancy
        fields = [
            'id',
            'title',
            'salary',
            'location',
            'description',
            'company',
            'candidate_count',
            'candidates',
            'type_slug',
            'status_name',
            'category',
            'tags',
        ]
