from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.authentication.models import AuthUser


class AuthUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom', {'fields': ('hobby',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom', {'fields': ('hobby',)}),
    )


admin.site.register(AuthUser, AuthUserAdmin)
