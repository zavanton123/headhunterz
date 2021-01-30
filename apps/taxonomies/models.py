from django.db import models
from django_extensions.db.fields import AutoSlugField

from apps.core.models import TimeTrackedModel


class Category(TimeTrackedModel):
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
        verbose_name_plural = 'categories'


class Tag(TimeTrackedModel):
    name = models.CharField(
        unique=True,
        max_length=100,
    )
    slug = AutoSlugField(
        populate_from=['name'],
    )

    def __str__(self):
        return self.name
