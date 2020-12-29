# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/12/11

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, response, status
from .serializers import GroupSerializer, UserGroupsSerializer
from .filters import GroupFilter

User = get_user_model()

class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_class = GroupFilter
    filter_fields = ("name",)


class UserGroupViewset(viewsets.GenericViewSet,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin):
    """
    retrive:
        获取当前用户所有的用户组列表
    update:
        修改当前用户角色
    """
    queryset = User.objects.all()
    serializer_class = UserGroupsSerializer

    def retrieve(self, request, *args, **kwargs):
        userObj = self.get_object()
        queryset = userObj.groups.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)



    def update(self, request, *args, **kwargs):
        userObj = self.get_object()
        groupIds = request.data.get("gids", [])
        userObj.groups = Group.objects.filter(id__in=groupIds)
        return response.Response(status=status.HTTP_204_NO_CONTENT)