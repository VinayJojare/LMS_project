from rest_framework import permissions
from Users.models import Teacher

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return Teacher.objects.filter(user=request.user).exists()