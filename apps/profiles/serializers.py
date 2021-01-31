import logging

from rest_framework import serializers

from apps.authentication.models import AuthUser
from apps.profiles.models import PersonProfile

log = logging.getLogger(__name__)


class PersonProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonProfile
        fields = [
            'id',
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
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        auth_user = AuthUser.objects.create_user(username=username, email=email, password=password)

        person = PersonProfile.objects.create(
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            gender=self.get_gender(validated_data),
            age=validated_data.get('age', 0),
            auth_user=auth_user
        )
        return person

    def update(self, instance, validated_data):
        pass

    def get_gender(self, validated_data):
        gender = validated_data.get('gender', '').lower()
        if gender == 'male':
            return 'M'
        elif gender == 'female':
            return 'F'
        else:
            return ''
