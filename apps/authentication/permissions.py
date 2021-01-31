from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_superuser
        )
