# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/6/29

from rest_framework import serializers
from .models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    """
    任务序列化类
    """

    class Meta:
        model = Tasks
        fields = "__all__"
