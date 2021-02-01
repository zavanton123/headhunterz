import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
    description = serializers.TimeField()
    type = serializers.CharField()
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )

    # def _create_type(self, *args, **kwargs):
    #     log.debug('zavanton - _create_type')
    #     return 1

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
        log.debug('zavanton - create')
        request = self.context.get('request', None)
        if request is None:
            raise ValidationError('request must not be None')
        user = request.user
        if not user.is_authenticated:
            raise ValidationError('user must be logged in')
        company = CompanyProfile.objects.get(auth_user=user)



        # type_slug = validated_data.pop('type')
        # vacancy_type = VacancyType.objects.filter(slug=type_slug).first()
        #
        # vacancy = Vacancy.objects.create(company=company, type=vacancy_type, **validated_data)
        log.debug('zavanton - ')
        return None
