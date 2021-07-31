# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/30

import django_filters
from .models import Escluster, Indexmanage

class EsclusterFilter(django_filters.FilterSet):
    """
    group 搜索过滤类
    """
    name = django_filters.CharFilter(lookup_expr="icontains")
    code = django_filters.CharFilter(lookup_expr="icontains")
    env = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Escluster
        fields = ["name", "code", "env"]


class IndexmanageFilter(django_filters.FilterSet):
    """
    group 搜索过滤类
    """
    cluster = django_filters.CharFilter(lookup_expr="icontains")
    name = django_filters.CharFilter(lookup_expr="icontains")
    saveDay = django_filters.CharFilter(lookup_expr="icontains")
    monitorSt = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Indexmanage
        fields = ["name", "cluster", "saveDay", "monitorSt"]
