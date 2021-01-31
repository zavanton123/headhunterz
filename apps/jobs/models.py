from django.db import models
from django_extensions.db.fields import AutoSlugField

from apps.core.models import TimeTrackedModel


class Vacancy(TimeTrackedModel):
    title = models.CharField(
        max_length=500,
    )
    slug = AutoSlugField(populate_from=('title',))
    salary = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True,
        blank=True,
        default=0.0,
    )
    location = models.CharField(
        max_length=500,
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
    )
    company = models.ForeignKey(
        to='profiles.CompanyProfile',
        on_delete=models.CASCADE,
        related_name='vacancies',
    )
    candidates = models.ManyToManyField(
        to='profiles.PersonProfile',
        related_name='applied_vacancies',
        through='Application',
    )
    favorites = models.ManyToManyField(
        to='profiles.PersonProfile',
        related_name='favorite_vacancies',
        null=True,
        blank=True,
    )
    type = models.ForeignKey(
        to='VacancyType',
        on_delete=models.CASCADE,
        related_name='vacancies',
    )
    status = models.ForeignKey(
        null=True,
        to='VacancyStatus',
        on_delete=models.SET_NULL,
        related_name='vacancies',
    )
    category = models.ForeignKey(
        to='taxonomies.Category',
        on_delete=models.CASCADE,
        related_name='vacancies',
    )
    tags = models.ManyToManyField(
        to='taxonomies.Tag',
        related_name='vacancies',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "vacancies"


class VacancyType(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
    )
    slug = AutoSlugField(populate_from=('title',))

    def __str__(self):
        return self.title


class VacancyStatus(models.Model):
    title = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'vacancy statuses'


class Application(TimeTrackedModel):
    candidate = models.ForeignKey(
        to='profiles.PersonProfile',
        on_delete=models.CASCADE,
    )
    vacancy = models.ForeignKey(
        to='Vacancy',
        on_delete=models.CASCADE,
    )
    feedback = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
    )
    status = models.ForeignKey(
        null=True,
        to='ApplicationStatus',
        on_delete=models.SET_NULL,
        related_name='applications'
    )


class ApplicationStatus(models.Model):
    title = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'application statuses'
