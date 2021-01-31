from rest_framework import viewsets, permissions

from apps.profiles.permissions import IsCompanyProfile
from apps.taxonomies.models import Tag, Category
from apps.taxonomies.serializers import TagSerializer, CategorySerializer


class TaxonomyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser | IsCompanyProfile]


class TagViewSet(TaxonomyViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryViewSet(TaxonomyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
