from django.contrib import admin

from .models import PersonProfile, CompanyProfile


@admin.register(PersonProfile)
class PersonProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'auth_user',
        'first_name',
        'last_name',
        'gender',
        'age',
    )
    list_filter = ('auth_user',)


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'auth_user', 'name', 'description', 'address')
    list_filter = ('auth_user',)
    search_fields = ('name',)
