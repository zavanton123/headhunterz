from django.template.defaultfilters import slugify
from rest_framework import serializers

from apps.taxonomies.models import Tag, Category


class TaxonomySerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = slugify(instance.name)
        instance.save()
        return instance


class TagSerializer(TaxonomySerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']
        read_only_fields = ('id', 'slug',)


class CategorySerializer(TaxonomySerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = ('id', 'slug',)
