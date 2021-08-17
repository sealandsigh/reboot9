# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/13

from django.shortcuts import render, HttpResponse
from .tasks import add

def index(request):
    res = add.delay(1,2)
    print(res)
    return HttpResponse("This is Ok! {}".format(res))

# 用户登录view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate
#
#
# class Login(APIView):
#
#     def post(self, request):
#         username = request.data.get('username', None)
#         password = request.data.get('password', None)
#         # 先验证ldap账户，如果不存在，则会验证本地用户
#         ldap_user = authenticate(username=username, password=password)
#         # 验证通过后，可以看到，本地user表中，会自动添加一条同步的用户信息
#         if ldap_user:
#             return Response(
#                 {'code': 200, 'uid': ldap_user.id, 'name': ldap_user.name, 'department': ldap_user.department}
#             )
#         return Response({'code': 405, 'message': '用户名或密码错误'})

