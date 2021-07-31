# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/7/29

from rest_framework import serializers
from .models import Escluster, Indexmanage

class EsclusterSerializer(serializers.ModelSerializer):
    """
    es集群序列化
    """

    class Meta:
        model = Escluster
        fields = "__all__"


class IndexmanageSerializer(serializers.ModelSerializer):
    """
    索引管理序列化
    """

    class Meta:
        model = Indexmanage
        fields = "__all__"
