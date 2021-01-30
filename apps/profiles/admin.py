from django.contrib import admin

from .models import Profile
from .models import ProfileType


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display_links = ('last_name',)
    ordering = ['id']
    list_display = (
        'id',
        'first_name',
        'last_name',
        'gender',
    )


@admin.register(ProfileType)
class ProfileTypeAdmin(admin.ModelAdmin):
    list_display_links = ('title',)
    ordering = ['id']
    list_display = (
        'id',
        'title',
        'description'
    )
