# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/20

from rest_framework import serializers
from .models import Idc

class IDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idc
        # fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        fields = "__all__"

class IdcSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name    = serializers.CharField(required=False, help_text="IDC名称", label="IDC名称")
    address = serializers.CharField(required=False, help_text="IDC地址", label="IDC地址")
    phone   = serializers.CharField(required=False, help_text="IDC联系电话", label="IDC联系电话")
    email   = serializers.EmailField(required=False, help_text="IDCemail", label="IDCemail")

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance

    def create(self, validated_data):
        return Idc.objects.create(**validated_data)