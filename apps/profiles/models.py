from django.db import models


class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M',
        FEMALE = 'F',

    auth_user = models.OneToOneField(
        to='authentication.AuthUser',
        on_delete=models.CASCADE,
        related_name='profiles',
    )
    first_name = models.CharField(
        max_length=100,
    )
    last_name = models.CharField(
        max_length=100,
    )
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.MALE,
    )
    type = models.ForeignKey(
        to='ProfileType',
        on_delete=models.CASCADE,
        related_name='profiles',
    )

    def __str__(self):
        return self.last_name


class ProfileType(models.Model):
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField(
        max_length=1000,
    )

    def __str__(self):
        return self.title
