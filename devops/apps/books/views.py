# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/6/1

from rest_framework import viewsets
# drf自带的分页
from rest_framework.pagination import PageNumberPagination
# drf自带的过滤器，提供了SearchFilter,OrderingFilter搜索和排序功能
from rest_framework import filters
# 第三方过滤器，高度可定制，DjangoFilterBackend 默认是精确(查找)过滤，即字段值必须要完全一样才能匹配成功
from django_filters.rest_framework import DjangoFilterBackend
# drf自带的三种用户认证方式
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
# jwt用户认证方式
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# drf自带的权限管理方式
from rest_framework.permissions import IsAuthenticated