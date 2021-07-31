# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/30

from rest_framework.routers import DefaultRouter
from .views import EsclusterViewSet, IndexmanageViewSet

esmanager_router = DefaultRouter()
esmanager_router.register("escluster", EsclusterViewSet, base_name="escluster")
esmanager_router.register("indexmanage", IndexmanageViewSet, base_name="indexmanage")
