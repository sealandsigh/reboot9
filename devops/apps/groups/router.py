# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/12/11

from rest_framework.routers import DefaultRouter
from .views import GroupViewset

group_router = DefaultRouter()
group_router.register('groups', GroupViewset, base_name="groups")