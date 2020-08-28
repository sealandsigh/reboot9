# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/20

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^idcs/$', views.idc_list),
    url(r'^idcs/(?P<pk>[0-9]+)/$', views.idc_detail),
]

############################ 版本二 ########################################
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^idcs/$', views.idc_list_v2, name="idc-list"),
    url(r'^idcs/(?P<pk>[0-9]+)/$', views.idc_detail_v2, name="idc-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

############################ 版本三 ########################################
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^idcs/$', views.IdcList.as_view(), name="idc-list"),
    url(r'^idcs/(?P<pk>[0-9]+)/$', views.IdcDetail.as_view(), name="idc-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

############################ 版本四 ########################################
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^idcs/$', views.IdcList_V4.as_view(), name="idc-list"),
    url(r'^idcs/(?P<pk>[0-9]+)/$', views.IdcDetail_V4.as_view(), name="idc-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

############################ 版本五 ########################################
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^idcs/$', views.IdcList_V5.as_view(), name="idc-list"),
    url(r'^idcs/(?P<pk>[0-9]+)/$', views.IdcDetail_V5.as_view(), name="idc-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

############################ 版本六 ########################################
from rest_framework.urlpatterns import format_suffix_patterns
idc_list = views.IdcViewSet.as_view({
    "get":"list",
    "post":"create",
})
idc_detail = views.IdcViewSet.as_view({
    "get": "retrieve",
    "put":"update",
    "delete":"destroy",
})

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^idcs/$', idc_list, name="idc-list"),
    url(r'^idcs/(?P<pk>[0-9]+)/$', idc_detail, name="idc-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

############################ 版本七 ########################################
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("idcs", views.IdcViewSet_V7)
urlpatterns = [
    url(r'^', include(router.urls))
]
