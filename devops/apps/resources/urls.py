# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/30

from django.conf.urls import url, include
from .views import TestView

urlpatterns = [
    url(r'^test/$', TestView.as_view()),
]