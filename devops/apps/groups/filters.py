# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/12/11

import django_filters
from django.contrib.auth.models import Group

class GroupFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Group
        fields = ["name"]