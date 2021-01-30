from django.db import models
from django_extensions.db.fields import AutoSlugField

from apps.core.models import TimeTrackedModel


class PersonProfile(TimeTrackedModel):
    class Gender(models.TextChoices):
        MALE = 'M',
        FEMALE = 'F',

    auth_user = models.OneToOneField(
        to='authentication.AuthUser',
        on_delete=models.CASCADE,
        related_name='person_profiles',
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=100,
    )
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        null=True,
        blank=True,
        default=Gender.MALE,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        default=18,
    )

    def __str__(self):
        return self.last_name


class CompanyProfile(TimeTrackedModel):
    auth_user = models.OneToOneField(
        to='authentication.AuthUser',
        on_delete=models.CASCADE,
        related_name='company_profiles',
    )
    name = models.CharField(
        max_length=500,
        unique=True,
    )
    slug = AutoSlugField(
        populate_from=('name',)
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
    )
    website = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
    )
    address = models.CharField(
        max_length=500,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
