from django.shortcuts import render
from .models import Idc
from .serializers import IdcSerializer, IDCSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse, HttpRequest


# Create your views here.

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        content = JSONRenderer().render(data)
        super(JSONResponse, self).__init__(content=content, **kwargs)

#/idcs/

def idc_list(request, *args, **kwargs):
    if request.method == "GET":
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return JSONResponse(serializer.data)
        # content = JSONRenderer().render(serializer.data)
        # return  HttpResponse(content, content_type="application/json")

    elif request.method == "POST":
        # 创建一个对象，并返回这个对象
        content = JSONParser().parse(request)
        serializer = IdcSerializer(data=content)
        if serializer.is_valid():
            serializer.save()
            # return JSONResponse(serializer.data)
            content = JSONRenderer().render(serializer.data)
            return HttpResponse(content, content_type="application/json")

# /idcs/pk
def idc_detail(request, pk, *args, **kwargs):
    try:
        idc = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        # 获取指定idc的详情记录
        serializer = IdcSerializer(idc)
        return JSONResponse(serializer.data)
    elif request.method == "PUT":
        # 修改一个对象
        content = JSONParser().parse(request)
        serializer = IdcSerializer(idc, data=content)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
    elif request.method == "DELETE":
        # 删除这个对象
        idc.delete()
        return HttpResponse(status=204)

#========================版本二===========================================
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])
def idc_list_v2(request, *args, **kwargs):
    if request.method == "GET":
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return Response(serializer.data)
        # content = JSONRenderer().render(serializer.data)
        # return  HttpResponse(content, content_type="application/json")

    elif request.method == "POST":
        # 创建一个对象，并返回这个对象
        content = JSONParser().parse(request)
        serializer = IdcSerializer(data=content)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT","DELETE"])
def idc_detail_v2(request, pk, *args, **kwargs):
    try:
        idc = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # 获取指定idc的详情记录
        serializer = IdcSerializer(idc)
        return Response(serializer.data)
    elif request.method == "PUT":
        # 修改一个对象
        content = JSONParser().parse(request)
        serializer = IdcSerializer(idc, data=content)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        # 删除这个对象
        idc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.reverse import reverse
@api_view(["GET"])
def api_root(request, format=None, *args, **kwargs):
    return Response({
        "idcs": reverse("idc-list", request=request, format=format)
    })

################################# 版本三 ###################################
from rest_framework.views import APIView
from django.http import Http404

class IdcList(APIView):
    def get(self, request, format=None):
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # content = JSONParser().parse(request)
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class IdcDetail(APIView):
    def get_object(self, pk):
        try:
            return Idc.objects.get(pk=pk)
        except Idc.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        idc = self.get_object(pk)
        serializer = IdcSerializer(idc)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        idc = self.get_object(pk)
        # content = JSONParser().parse(request)
        serializer = IdcSerializer(idc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        idc = self.get_object(pk)
        idc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################################ 版本四 #########################################
from rest_framework import mixins, generics

class IdcList_V4(generics.GenericAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class IdcDetail_V4(generics.GenericAPIView,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

################################ 版本五 #########################################

class IdcList_V5(generics.ListCreateAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

class IdcDetail_V5(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

################################ 版本六 #########################################
from rest_framework import viewsets
class IdcViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

################################ 版本七 #########################################
class IdcViewSet_V7(viewsets.ModelViewSet):
    """
    retrieve:
        获取指定IDC记录
    list:
        获取idc列表
    update:
        更新idc记录
    portial_update:
        更新idc的部分记录
    destroy:
        删除idc记录
    create:
        增加一条idc记录
    """
    queryset = Idc.objects.all()
    # serializer_class = IdcSerializer
    serializer_class = IDCSerializer