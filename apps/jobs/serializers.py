import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from apps.jobs.models import VacancyType, VacancyStatus, Vacancy
from apps.profiles.models import PersonProfile, CompanyProfile
from apps.profiles.serializers import CompanySerializer
from apps.taxonomies.models import Category
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


class CreateVacancySerializer(serializers.Serializer):
    title = serializers.CharField()
    salary = serializers.DecimalField(
        max_digits=20,
        decimal_places=2,
    )
    location = serializers.CharField()
    description = serializers.CharField()
    type = serializers.CharField()
    category = serializers.CharField()

    class Meta:
        model = Vacancy
        fields = [
            'title',
            'salary',
            'location',
            'description',
            'type',
            'category',
            # 'tags',
        ]

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request is None:
            raise ValidationError('request must not be None')
        user = request.user
        if not user.is_authenticated:
            raise ValidationError('user must be logged in')
        company = CompanyProfile.objects.get(auth_user=user)

        log.debug('zavanton - create')
        title = validated_data.get('title', None)
        salary = validated_data.get('salary', None)
        location = validated_data.get('location', None)
        description = validated_data.get('description', None)
        type_slug = validated_data.get('type', None)
        category_slug = validated_data.get('category', None)

        vacancy_status = VacancyStatus.objects.filter(title__icontains='unfilled').first()
        vacancy_type = get_object_or_404(VacancyType, slug=type_slug)

        category = get_object_or_404(Category, slug=category_slug)

        return Vacancy.objects.create(
            title=title,
            salary=salary,
            location=location,
            description=description,
            company=company,
            type=vacancy_type,
            status=vacancy_status,
            category=category
        )

    def update(self, instance, validated_data):
        pass
