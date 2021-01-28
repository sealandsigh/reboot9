# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/12/11

import django_filters
from django.contrib.auth.models import Group

class GroupFilter(django_filters.FilterSet):
    """
    group 搜索过滤类
    """
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Group
        fields = ["name"]
        # 原代码中是元组, 这里用列表貌似也没问题。
        # fields = (name,)