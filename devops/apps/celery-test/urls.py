# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/13

from django.conf.urls import url, include
from .views import index

urlpatterns = [
    url(r'^celery-test/$', index),
]
