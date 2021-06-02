# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/6/1

import django_filters
from .models import Publish, Author, Book

class PublishFilter(django_filters.FilterSet):
    """
    group 搜索过滤类
    """
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Publish
        fields = ["name"]
        # 原代码中是元组, 这里用列表貌似也没问题。
        # fields = (name,)


class AuthorFilter(django_filters.FilterSet):
    """
    group 搜索过滤类
    """
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Author
        fields = ["name"]
        # 原代码中是元组, 这里用列表貌似也没问题。
        # fields = (name,)


class BookFilter(django_filters.FilterSet):
    """
    group 搜索过滤类
    """
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Book
        fields = ["name"]
        # 原代码中是元组, 这里用列表貌似也没问题。
        # fields = (name,)