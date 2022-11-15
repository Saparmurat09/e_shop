from rest_framework import permissions


class StaffPermissions(permissions.BasePermission):

    edit_methods = ["PUT", "POST", "DELETE", "GET"]

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permissions(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.user == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False

        #


class AdminPermissions(permissions.BasePermission):
    edit_methods = [
        'PUT',
        'DELETE',
        'POST',
        'GET',
    ]

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permissions(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.user == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False
