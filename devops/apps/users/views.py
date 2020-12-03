# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/25

from rest_framework import viewsets, permissions, mixins
from .serializers import UserSerializer, UserRegSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserFilter
from django.contrib.auth import get_user_model
User = get_user_model()

class UserViewset(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
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
    # pagination_class.page_query_param = "p"
    # pagination_class.page_size_query_param = "page_size"

    # 最基本的搜索，示例，但是我们肯定不用
    # def get_queryset(self):
    #     queryset = super(UserViewset, self).get_queryset()
    #     queryset = queryset.filter(username__icontains=self.request.query_params.get("username"))
    #     return queryset

    # filter_backends = (DjangoFilterBackend,)
    # permission_classes = (permissions.IsAuthenticated, permissions.DjangoModelPermissions)
    filter_class = UserFilter
    filter_fields = ("username",)

class UserRegViewset(viewsets.GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin):
    """
    create:
        用户注册
    partial_update:
        修改密码
    update:
        修改密码
    """
    queryset = User.objects.all()
    serializer_class = UserRegSerializer
