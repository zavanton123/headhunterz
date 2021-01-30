from django.db import models
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
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


class Tag(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100,
    )
    slug = AutoSlugField(
        populate_from=['name'],
    )

    def __str__(self):
        return self.name
