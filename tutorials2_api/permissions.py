import copy

from rest_framework import serializers, permissions


# DEFAULT DjangoModelPermissions ALLOWS GET EVEN IF
# IT DOES NOT HAVE VIEW_PERMISSION,
# SOLUTION BELOW ADDRESSES IT
from rest_framework.permissions import BasePermission


class CustomDjangoModelPermission(permissions.DjangoModelPermissions):

    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


class IsGroupUser(BasePermission):
    group = None

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.groups.filter(name=self.group).exists()


class IsStudent(IsGroupUser):
    group = 'Student'