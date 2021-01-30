from rest_framework import serializers

from apps.profiles.models import PersonProfile


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
