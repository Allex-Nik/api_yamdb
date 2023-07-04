from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    message = 'Действие доступно только для автора.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.is_admin
            or request.method in permissions.SAFE_METHODS
        )


class Admin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class AdminModeratorOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        if request.user.is_authenticated:
            return request.user.is_admin or request.user.is_moderator
        return request.method in permissions.SAFE_METHODS
