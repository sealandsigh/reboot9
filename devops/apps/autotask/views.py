# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/6/29

from rest_framework import viewsets, permissions, response, status
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
from datetime import datetime
from utils.ansible_api import ANSRunner
import time
import json

# 引入自定义的模型，序列化，过滤器类
from .models import Tasks
from .serializers import TasksSerializer


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class TasksViewset(viewsets.ModelViewSet):
    """
    create:
    创建任务
    list:
    获取任务列表
    retrieve:
    获取任务信息
    update:
    执行任务
    """

    # 用户认证及权限验证(四种用户模式按顺序依次匹配)
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication,
                              SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, permissions.DjangoModelPermissions)

    # 查询结果集
    queryset = Tasks.objects.all()
    # 使用序列化
    serializer_class = TasksSerializer
    # 调用分页类
    pagination_class = Pagination
    # 定义过滤器
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 调用过滤类
    # filter_class = PublishFilter
    search_fields = ('name',)
    ordering_fields = ('id',)

    def partial_update(self, request, *args, **kwargs):
        """
        执行任务，并将结果入库
        """
        pk = int(kwargs.get("pk"))
        data = request.data
        print(data)
        task = Tasks.objects.get(pk=pk)
        rbt = ANSRunner()
        print(task.playbook.path)
        rbt.run_playbook(task.playbook.path)
        data['detail_result'] = json.dumps(rbt.get_playbook_result(), indent=4)
        data["exec_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        Tasks.objects.filter(pk=pk).update(**data)
        return response.Response(status=status.HTTP_204_NO_CONTENT)
