import logging

from django.template.defaultfilters import slugify
from rest_framework import serializers

from apps.authentication.models import AuthUser
from apps.profiles.models import PersonProfile, CompanyProfile

log = logging.getLogger(__name__)


def get_gender(validated_data, default=''):
    gender = validated_data.get('gender').lower()
    if gender == 'male':
        return 'M'
    elif gender == 'female':
        return 'F'
    else:
        return default


class PersonSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source='auth_user.username',
    )
    email = serializers.CharField(
        source='auth_user.email',
    )

    class Meta:
        model = PersonProfile
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'gender',
            'age',
            'created_at',
            'updated_at',
        ]


class CreatePersonSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        write_only=True,
    )
    email = serializers.EmailField(
        required=True,
        write_only=True,
    )
    # todo zavanton - add password validation
    password = serializers.CharField(
        required=True,
        write_only=True,
    )
    first_name = serializers.CharField(
        max_length=100,
    )
    last_name = serializers.CharField(
        max_length=100,
        required=True,
    )
    gender = serializers.CharField(
        max_length=6,
    )
    age = serializers.IntegerField()

    def create(self, validated_data):
        auth_user = AuthUser.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )

        person = PersonProfile.objects.create(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            gender=get_gender(validated_data),
            age=validated_data.get('age'),
            auth_user=auth_user
        )
        return person

    def update(self, instance, validated_data):
        user = instance.auth_user
        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        user.save()

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.gender = get_gender(validated_data, default=instance.gender)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance


class UpdatePersonSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(
        max_length=6,
    )

    class Meta:
        model = PersonProfile
        fields = [
            'first_name',
            'last_name',
            'gender',
            'age',
        ]
        write_only_fields = [
            'first_name',
            'last_name',
            'gender',
            'age',
        ]

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        gender = get_gender(validated_data, default=instance.gender)
        instance.gender = gender
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance


class CompanySerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    def get_username(self, company, *args, **kwargs):
        return company.auth_user.username

    def get_email(self, company, *args, **kwargs):
        return company.auth_user.email

    class Meta:
        model = CompanyProfile
        fields = [
            'id',
            'username',
            'email',
            'name',
            'slug',
            'description',
            'website',
            'address',
        ]


class CreateCompanySerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        write_only=True,
    )
    email = serializers.EmailField(
        write_only=True
    )
    # todo zavanton - add validation
    password = serializers.CharField(
        write_only=True,
    )

    class Meta:
        model = CompanyProfile
        fields = [
            'username',
            'email',
            'password',
            'name',
            'description',
            'website',
            'address',
        ]

    def create(self, validated_data):
        auth_user = AuthUser.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )
        company = CompanyProfile.objects.create(
            auth_user=auth_user,
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            website=validated_data.get('website'),
            address=validated_data.get('address')
        )
        return company

    def update(self, instance, validated_data):
        user = instance.auth_user
        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        user.save()

        instance.name = validated_data.get('name', instance.name)
        instance.slug = slugify(instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.website = validated_data.get('website', instance.website)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
