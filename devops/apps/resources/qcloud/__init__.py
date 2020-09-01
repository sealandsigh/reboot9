# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/27

from tencentcloud.common import credential
from django.conf import settings

def getCredential():
    return credential.Credential(settings.QCLOUD_SECRETID, settings.QCLOUD_SECRETKEY)