# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/25

from rest_framework import serializers
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions')