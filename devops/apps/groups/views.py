# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/12/11

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, response, status
from .serializers import GroupSerializer, UserGroupsSerializer
from .filters import GroupFilter
from users.serializers import UserSerializer

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


class GroupMembersViewset(viewsets.GenericViewSet,
                          mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin):
    """
    角色成员管理
    retrieve:
        获取指定组下的成员列表

    """
    queryset = Group.objects.all()
    serializer_class = UserSerializer
    def retrieve(self, request, *args, **kwargs):
        groupobj = self.get_object()
        queryset = groupobj.user_set.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        groupObj = self.get_object()
        userId = request.data.get("uid", 0)
        ret = {"status": 0}
        try:
            userObj = User.objects.get(pk=userId)
            groupObj.user_set.remove(userObj)
        except User.DoesNotExist:
            ret["status"] = 1
            ret["errmsg"] = "用户错误"
        return response.Response(ret, status=status.HTTP_200_OK)