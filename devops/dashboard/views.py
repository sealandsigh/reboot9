from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse, QueryDict
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.views.generic import TemplateView
from django.core import serializers
from django.http import Http404

import json
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    data = ["a", "b", "c"]
    dataD = {"a":"b", "c":"d"}
    # return HttpResponse(json.dumps(data))
    # 列表类型 safe 为 False
    # return JsonResponse(data, safe=False)
    # 字典类型 safe 为 true
    # return JsonResponse(dataD)

    if request.method == "GET":
        print(request.GET)
        print(request.GET.getlist("cc"))
    elif request.method == "POST":
        print(request.POST)
    elif request.method == "DELETE":
        print("request delete:", QueryDict(request.body))
    return HttpResponse('')

# def login(request):
#     username = request.POST.get("username", None)
#     userpass = request.POST.get("userpass", None)
#     if username == "admin" and userpass == "123456":
#         msg = "登录成功"
#         print("登录成功")
#     else:
#         msg = "登录失败"
#         print("登录失败")
#     return HttpResponse(msg)

def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        userpass = request.POST.get("userpass", None)
        # try:
        #     User.objects.get(username=username)
        # except User.DoesNotExist:
        #     return HttpResponse("用户不存在")

        user = authenticate(request, username=username, password=userpass)
        if user is not None:
            login(request, user)
            return HttpResponse("用户登录成功")
        else:
            return HttpResponse("用户登录失败")
    return render(request, "login.html")

def article(request, *args, **kwargs):
    # return HttpResponse(json.dumps(args))
    # return JsonResponse(kwargs,safe=False)
    return JsonResponse(args,safe=False)

class LoginView(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        kwargs['title'] = "reboot"
        return kwargs

    def get(self, request, *args, **kwargs):
        return HttpResponse("展示用户登录页")

    def post(self, request, *args, **kwargs):
        return HttpResponse('验证用户名和密码')

class UserView(View):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace', 'list']
    def get(self, request, *args, **kwargs):
        per = 10
        try:
            page = int(request.GET.get("page", "1"))
        except:
            page = 1

        if page < 1:
            page = 1

        end = page * per
        start = end - per
        queryset = User.objects.all()[start:end]
        data = [{"userid":user.id, "email":user.email, "username":user.username} for user in  queryset]
        print(queryset)
        return JsonResponse(data,safe=False)

    def post(self, request, *args, **kwargs):
        return HttpResponse("修改用户信息")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("删除用户信息")

    def put(self, request, *args, **kwargs):
        return HttpResponse("添加用户信息")

    def list(self, request, *args, **kwargs):
        return HttpResponse("list用户信息")

class UserView2(View):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        paginator = Paginator(queryset, 10)
        try:
            page = int(request.GET.get("page", "1"))
        except:
            page = 1

        if page < 1:
            page = 1
        page = paginator.page(page)

        data = [{"userid":user.id, "email":user.email, "username":user.username} for user in  page.object_list]
        print(queryset)
        return JsonResponse(data,safe=False)

class UserView3(View):

    def post(self, request, *args, **kwargs):
        logger.debug("创建用户")
        # 1 获取提交过来的参数
        # username = request.POST.get("username")
        # userpass = request.POST.get("userpass")
        # email = request.POST.get("email")
        data = request.POST.dict()
        logger.debug("请求数据转dict")
        print(data)

        # 2 验证参数，所有的参数不能为空
        # if not username or not userpass or not email:
        #     return JsonResponse({"errmsg":"参数有误"})
        try:
            logger.debug("执行用户创建")
            user = User.objects.create_user(**data)
        except IntegrityError:
            logger.error("用户已存在")
            return JsonResponse({"errmsg": "用户已存在"})

        return JsonResponse({"id":user.id, "email":user.email, "username":user.username})


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Index View')


class GroupListView(View):
    def get(self, request, *args, **kwargs):
        queryset = Group.objects.all()
        return HttpResponse(serializers.serialize("json", queryset), content_type="application/json")


class GroupMembersView(View):
    def get_queryset(self):
        groupObj = self.get_group_obj()
        return  groupObj.user_set.all()

    def get_group_obj(self):
        try:
            groupObj = Group.objects.get(name=self.request.GET.get("name"))
        except Group.DoesNotExist:
            raise Http404
        except Group.MultipleObjectsReturned:
            raise Http404
        return groupObj

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return HttpResponse(serializers.serialize("json", queryset), content_type="application/json")


class UserGroupView(View):
    def get_queryset(self):
        userObj = self.get_user_obj()
        return  userObj.groups.all()

    def get_user_obj(self):
        try:
            userObj = User.objects.get(username=self.request.GET.get("username"))
        except User.DoesNotExist:
            raise Http404
        except User.MultipleObjectsReturned:
            raise Http404
        return userObj

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return HttpResponse(serializers.serialize("json", queryset), content_type="application/json")


class UserGroupManageView(View):
    def get_user_obj(self):
        try:
            userObj = User.objects.get(username=QueryDict(self.request.body).get("username"))
        except User.DoesNotExist:
            raise Http404
        except User.MultipleObjectsReturned:
            raise Http404
        return userObj

    def get_group_obj(self):
        try:
            groupObj = Group.objects.get(name=QueryDict(self.request.body).get("groupname"))
        except Group.DoesNotExist:
            raise Http404
        except Group.MultipleObjectsReturned:
            raise Http404
        return groupObj

    def delete(self, request, *args, **kwargs):
        """
        将用户从用户组中删除
        """
        groupObj = self.get_group_obj()
        userObj = self.get_user_obj()
        groupObj.user_set.remove(userObj)
        return HttpResponse("")

    def put(self, request, *args, **kwargs):
        """
        将用户从用户组中删除
        """
        groupObj = self.get_group_obj()
        userObj = self.get_user_obj()
        groupObj.user_set.add(userObj)
        return HttpResponse("")