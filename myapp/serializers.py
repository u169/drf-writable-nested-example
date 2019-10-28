from drf_writable_nested import NestedUpdateMixin, UniqueFieldsMixin
from rest_framework import serializers

from . import models


class UserSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('pk', 'name', 'first_name', 'last_name', 'age')


class GroupSerializer(NestedUpdateMixin, serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = models.Group
        fields = ('pk', 'title', 'users')
