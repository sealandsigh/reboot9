# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/12/11

from django.contrib.auth.models import Group
from rest_framework import viewsets, mixins
from .serializers import GroupSerializer
from .filters import GroupFilter


class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_class = GroupFilter
    filter_fields = ("name",)