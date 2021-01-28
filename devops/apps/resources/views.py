# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/30

from django.views import View
from django.http import  HttpResponse
from resources.qcloud import cvm
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Server
from .serializers import ServerSerializer
from resources.apscheduler import scheduler
import datetime


def runjob():
    print("runjob is run: {}".format(datetime.datetime.now()))

class TestView(View):
    def get(self, request, *args, **kwargs):
        cvm.getCvmlist()
        # scheduler.add_job(runjob, run_date=datetime.datetime.now(), id="runjob")
        return HttpResponse("")

class ServerViewset(ReadOnlyModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer