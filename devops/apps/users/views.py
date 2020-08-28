# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/25

from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination

class UserViewset(viewsets.ModelViewSet):
    """
        retrieve:
            获取指定user记录
        list:
            获取user列表
        update:
            更新user记录
        portial_update:
            更新user的部分记录
        destroy:
            删除user记录
        create:
            增加一条user记录
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # pagination_class = PageNumberPagination