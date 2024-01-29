from rest_framework import permissions


class IsOwnerOrReceiver(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.receiver == request.user
