from django.contrib import admin

from .models import Application, ApplicationStatus
from .models import Vacancy, VacancyType, VacancyStatus


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display_links = ('title',)
    list_display = (
        'id',
        'title',
        'salary',
        'location',
        'description',
        'company',
        'type',
        'category',
    )
    list_filter = ('company', 'type', 'category')


@admin.register(VacancyType)
class VacancyTypeAdmin(admin.ModelAdmin):
    list_display_links = ('title',)
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(VacancyStatus)
class VacancyStatusAdmin(admin.ModelAdmin):
    list_display_links = ('title',)
    list_display = ('id', 'title')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'candidate',
        'vacancy',
        'feedback',
        'status',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'candidate',
        'vacancy',
        'status',
    )
    date_hierarchy = 'created_at'


@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
