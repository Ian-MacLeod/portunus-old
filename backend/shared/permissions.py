from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from rest_framework import permissions


def has_auth_or_oauth_permission(has_auth_permission, request, view):
    oauth2_authenticated = isinstance(request.successful_authenticator, OAuth2Authentication)

    return (
        has_auth_permission and not oauth2_authenticated
    ) or TokenHasReadWriteScope().has_permission(request, view)


class IsSameUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        has_auth_permission = request.user and (obj == request.user or request.user.is_staff)

        return has_auth_or_oauth_permission(has_auth_permission, request, view)


class IsSameUserOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        has_auth_permission = request.user and (
            obj == request.user or request.user.is_superuser
        )

        return has_auth_or_oauth_permission(has_auth_permission, request, view)


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        has_auth_permission = permissions.IsAdminUser().has_permission(request, view)

        return has_auth_or_oauth_permission(has_auth_permission, request, view)
