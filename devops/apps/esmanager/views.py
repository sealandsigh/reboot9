# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/30

from rest_framework import viewsets, permissions
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

# 引入自定义的模型，序列化，过滤器类
from .models import Escluster, Indexmanage
from .serializers import EsclusterSerializer, IndexmanageSerializer
from .filters import EsclusterFilter, IndexmanageFilter


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class EsclusterViewSet(viewsets.ModelViewSet):
    """
    list:
        列出所有集群信息
    retrieve:
        某个集群的详细信息
    create:
        创建集群
    update:
        更新集群
    delete:
        删除集群
    """

    # 用户认证及权限验证(四种用户模式按顺序依次匹配)
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication,
                              SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, permissions.DjangoModelPermissions)

    # 查询结果集
    queryset = Escluster.objects.all()
    # 使用序列化
    serializer_class = EsclusterSerializer
    # 调用分页类
    pagination_class = Pagination
    # 定义过滤器
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 调用过滤类
    filter_class = EsclusterFilter
    search_fields = ('name', 'code', 'env')
    ordering_fields = ('code',)


class IndexmanageViewSet(viewsets.ModelViewSet):
    """
    list:
        列出所有集群信息
    retrieve:
        某个集群的详细信息
    create:
        创建集群
    update:
        更新集群
    delete:
        删除集群
    """

    # 用户认证及权限验证(四种用户模式按顺序依次匹配)
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication,
                              SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, permissions.DjangoModelPermissions)

    # 查询结果集
    queryset = Indexmanage.objects.all()
    # 使用序列化
    serializer_class = IndexmanageSerializer
    # 调用分页类
    pagination_class = Pagination
    # 定义过滤器
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 调用过滤类
    filter_class = IndexmanageFilter
    search_fields = ('name', 'cluster__code', 'saveDay', 'monitorSt')
    ordering_fields = ('saveDay', 'createTime')

