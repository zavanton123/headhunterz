from django.urls import path, include
from rest_framework import routers

from apps.taxonomies.views import TagViewSet, CategoryViewSet

app_name = 'taxonomies'

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls))
]
