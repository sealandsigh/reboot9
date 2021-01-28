# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/9/1

from rest_framework.routers import DefaultRouter
from .views import ServerViewset

router = DefaultRouter()
router.register("servers", ServerViewset, base_name="servers")