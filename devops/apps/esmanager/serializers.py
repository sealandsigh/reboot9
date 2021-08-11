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
        depth = 1

    # 此处加上depth即可，如果不需要展示那么多，可以用下面的序列化方法
    # def to_escluster_response(self, escluster_queryset):
    #     ret = []
    #     for escluster in escluster_queryset:
    #         ret.append({
    #             'id': escluster.id,
    #             'name': escluster.name,
    #             'code': escluster.code
    #         })
    #     return ret

    # def to_representation(self, instance):
    #     # escluster = self.to_escluster_response(instance.cluster.all())
    #     ret = super(IndexmanageSerializer, self).to_representation(instance)
    #     # ret["escluster"] = escluster
    #     return ret

