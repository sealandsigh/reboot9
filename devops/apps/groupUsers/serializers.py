# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/24

from rest_framework import serializers
from django.contrib.auth.models import Group

class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False)