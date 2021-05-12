# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/4/28

from rest_framework import viewsets, mixins, response, status
from django.contrib.auth.models import Permission, Group
from .serializers import PermissionSerializer

class PermissionViewset(viewsets.GenericViewSet,
                        mixins.ListModelMixin):
    """
    权限列表
    list:
        获取权限列表
    """

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class GroupPermissionViewset(viewsets.GenericViewSet,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin):
    """
    用户组的权限
    retrieve:
        返回用户组的权限列表
    """
    queryset = Group.objects.all()
    serializer_class = PermissionSerializer

    def retrieve(self, request, *args, **kwargs):
        groupObj = self.get_object()
        queryset = groupObj.permissions.all()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


    def update(self, request, *args, **kwargs):
        ret = {"status":0}
        groupObj = self.get_object()
        pids = request.data.get("pids", [])
        groupObj.permissions = Permission.objects.filter(pk__in=pids)
        return response.Response(ret, status=status.HTTP_200_OK)
