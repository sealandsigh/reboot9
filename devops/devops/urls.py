"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from groupUsers.views import GroupUsersViewset
from idc.urls import router as idc_router
from users.router import router as user_router
from resources.router import router as resources_router
from resources.apscheduler import scheduler

router = DefaultRouter()
router.register("groupUsers", GroupUsersViewset, base_name="groupUsers")
router.registry.extend(idc_router.registry)
router.registry.extend(user_router.registry)
router.registry.extend(resources_router.registry)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include("resources.urls")),
    url(r'^docs/', include_docs_urls("接口文档"))
]