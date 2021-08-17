# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/13

from django.conf.urls import url, include
from .views import index
# from .views import Login

urlpatterns = [
    url(r'^celery-test/$', index),
    # url(r'^celery-test/$', Login.as_view()),
]
