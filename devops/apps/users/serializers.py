# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/25

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions')