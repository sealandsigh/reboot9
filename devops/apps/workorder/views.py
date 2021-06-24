# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/6/17

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
from .models import WorkOrder
from .serializers import WorkOrderSerializer


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class WorkOrderViewset(viewsets.ModelViewSet):
    """
    create:
        创建工单
    list:
        获取工单列表
    retrieve:
        某个工单详细信息
    update:
        更新工单
    delete:
        删除工单
    """
    # 用户认证及权限验证(四种用户模式按顺序依次匹配)
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication,
                              SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, permissions.DjangoModelPermissions)

    # 查询结果集
    queryset = WorkOrder.objects.all()
    # 使用序列化
    serializer_class = WorkOrderSerializer
    # 调用分页类
    pagination_class = Pagination
    # 定义过滤器
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 调用过滤类
    # filter_class = PublishFilter
    search_fields = ('title', 'order_contents')
    ordering_fields = ('id',)

    # def get_queryset(self):
    #     status = self.request.GET.get('status', None)
    #     print('status is {}'.format(status))
