# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/12/11

from django.contrib.auth.models import Group
from rest_framework import  serializers

class GroupSerializer(serializers.ModelSerializer):
    """
    group序列化类
    """

    def to_representation(self, instance):
        ret = super(GroupSerializer, self).to_representation(instance)
        ret["members"] = instance.user_set.count()
        return ret

    class Meta:
        model = Group
        fields = ("id", "name")


class UserGroupsSerializer(serializers.Serializer):
    """
    group序列化类
    """
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()

    class Meta:
        model = Group
        fields = ("id", "name")