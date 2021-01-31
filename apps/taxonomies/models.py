from django.db import models
from django_extensions.db.fields import AutoSlugField

from apps.core.models import TimeTrackedModel


class Taxonomy(TimeTrackedModel):
    name = models.CharField(
        unique=True,
        max_length=100,
    )
    slug = AutoSlugField(
        populate_from=['name'],
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(Taxonomy):
    class Meta:
        verbose_name_plural = 'categories'


class Tag(Taxonomy):
    class Meta:
        verbose_name_plural = 'tags'
