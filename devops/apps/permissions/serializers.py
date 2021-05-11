# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/4/28

from rest_framework import serializers
from django.contrib.auth.models import Permission

class PermissionSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = {}
        ret["key"] = instance.id
        ret["label"] = "{}.{}".format(instance.content_type.app_label, instance.codename)
        return ret

    class Meta:
        model = Permission
        fields = "__all__"