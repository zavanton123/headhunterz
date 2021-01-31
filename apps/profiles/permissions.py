from rest_framework import permissions

from apps.profiles.models import CompanyProfile, PersonProfile


class IsPersonProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return PersonProfile.objects.filter(auth_user=request.user).count() > 0
        return False


class IsCompanyProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return CompanyProfile.objects.filter(auth_user=request.user).count() > 0
        return False
