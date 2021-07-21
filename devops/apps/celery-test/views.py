# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/13

from django.shortcuts import render, HttpResponse
from .tasks import add

def index(request):
    res = add.delay(1,2)
    print(res)
    return HttpResponse("This is Ok! {}".format(res))

