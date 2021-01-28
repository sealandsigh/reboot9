# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/25
from rest_framework.routers import DefaultRouter
from .views import UserViewset, UserRegViewset

router = DefaultRouter()
router.register("users", UserViewset, base_name="users")
router.register("userReg", UserRegViewset, base_name="userReg")