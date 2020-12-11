# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/12/11

from django.contrib.auth.models import Group
from rest_framework import  serializers

class GroupSerializer(serializers.ModelSerializer):
    """
    group序列化类
    """
    class Meta:
        model = Group
        fields = ("id", "name")