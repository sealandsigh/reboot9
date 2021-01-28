# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/12
from django.conf.urls import url, include
from .views import index, loginView, article
from . import views

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', loginView, name="login"),
    url(r'^article/(?P<year>[0-9]{4})/([0-9]{2})/([0-9]{2})/$', article, name="article"),
    url(r'^index/$', views.IndexView.as_view(), name="IndexView"),
    url(r'^login/$', views.LoginView.as_view(), name="LoginView"),
    url(r'^user/$', views.UserView3.as_view(), name="UserView"),
    url(r'^grouplist/$', views.GroupListView.as_view(), name="GroupListView"),
    url(r'^groupmembers/$', views.GroupMembersView.as_view(), name="GroupMembersView"),
    url(r'^usergroups/$', views.UserGroupView.as_view(), name="UserGroupView"),
    url(r'^usergroupmanage/$', views.UserGroupManageView.as_view(), name="UserGroupManageView"),
]