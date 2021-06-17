# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/6/17

from rest_framework.routers import DefaultRouter
from .views import WorkOrderViewset

workorfer_router = DefaultRouter()
workorfer_router.register("workorder", WorkOrderViewset, base_name="workorder")
