# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/24

from rest_framework import viewsets, mixins, response, status
from django.contrib.auth.models import Group, User
from rest_framework.response import Response

from .serializers import UserSerializer, GroupSerializer

class GroupUsersViewset(viewsets.GenericViewSet, mixins.CreateModelMixin):
    # queryset = Group.objects.all()
    serializer_class = UserSerializer

    def get_group_object(self):
        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        # assert lookup_url_kwarg in self.kwargs, (
        #     'Expected view %s to be called with a URL keyword argument '
        #     'named "%s". Fix your URL conf, or set the `.lookup_field` '
        #     'attribute on the view correctly.' %
        #     (self.__class__.__name__, lookup_url_kwarg)
        # )

        # 相当于url里面的pk
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        return Group.objects.get(**filter_kwargs)

    def get_queryset(self):
        groupObj = self.get_group_object()
        return groupObj.user_set.all()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        groupObj = Group.objects.get(pk=request.data["gid"])
        userObj = User.objects.get(pk=request.data["uid"])
        groupObj.user_set.add(userObj)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        groupObj = self.get_group_object()
        userObj = User.objects.get(pk=request.data["uid"])
        groupObj.user_set.remove(userObj)
        return response.Response(status=status.HTTP_204_NO_CONTENT)