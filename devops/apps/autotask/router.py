# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/6/29

from rest_framework.routers import DefaultRouter
from .views import TasksViewset

autotask_router = DefaultRouter()
autotask_router.register("task", TasksViewset, base_name="task")
