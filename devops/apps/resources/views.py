# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/30

from django.views import View
from django.http import  HttpResponse
from resources.qcloud import cvm

class TestView(View):
    def get(self, request, *args, **kwargs):
        cvm.getCvmlist()
        return HttpResponse("")