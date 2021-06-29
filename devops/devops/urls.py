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
from rest_framework_jwt.views import obtain_jwt_token
# from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from groupUsers.views import GroupUsersViewset
# from idc.urls import router as idc_router
from users.router import router as user_router
from groups.router import group_router
from permissions.router import permission_router
from books.router import books_router
from workorder.router import workorfer_router
from autotask.router import autotask_router
from resources.router import router as resources_router
# from resources.apscheduler import scheduler

router = DefaultRouter()
# router.register("groupUsers", GroupUsersViewset, base_name="groupUsers")
# router.registry.extend(idc_router.registry)
router.registry.extend(user_router.registry)
router.registry.extend(group_router.registry)
# router.registry.extend(resources_router.registry)
router.registry.extend(permission_router.registry)
router.registry.extend(books_router.registry)
router.registry.extend(workorfer_router.registry)
router.registry.extend(autotask_router.registry)

from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^', include("resources.urls")),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', include_docs_urls("接口文档")),
    url(r'^api-token-auth/', obtain_jwt_token),
]