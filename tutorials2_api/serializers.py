import json

from django.contrib.auth.models import Permission
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from tutorials2_books.models_base import Books


def get_user_permissions(user):
    if user.is_superuser:
        return Permission.objects.all()
    return user.user_permissions.all() | Permission.objects.filter(group__user=user)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email

        permissions = get_user_permissions(user=self.user)
        permissions = list(permissions.values())
        print(permissions)

        # CHECK IF USER HAS PERMISSION
        # if request.user.has_perm('app_name.code_value'):
        if self.user.has_perm('tutorials2_books.can_sell'):
            print('User has Permission to Sell Books')

        # permissions = self.user.user_permissions.all().values()
        # permissions = list(permissions)
        # print(permissions)
        data['permissions'] = permissions
        return data
