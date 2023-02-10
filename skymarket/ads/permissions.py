from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomAdPermission(BasePermission):
    message = "You don't have permission to such action"

    def has_object_permission(self, request, view, obj):
        if request.user == (obj.author if obj.author else obj.owner):
            return True
        else:
            return request.user.role == "admin"


class CustomCommentPermission(BasePermission):
    message = "You don't have permission to such action"

    def has_object_permission(self, request, view, obj):
        if request.user == (obj.author if obj.author else obj.owner):
            return True
        else:
            return request.user.is_admin
