# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/8/25

from rest_framework import serializers
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'groups', 'user_permissions')


class UserRegSerializer(serializers.ModelSerializer):
    """
    用户注册序列化类
    """
    id       = serializers.IntegerField(read_only=True)
    name     = serializers.CharField(max_length=32, label="姓名", help_text="用户姓名，中文姓名")
    username = serializers.CharField(max_length=32, label="用户名", help_text="用户名，用户登陆名")
    password = serializers.CharField(style={"input_type": "password"}, label="密码", write_only=True, help_text="密码")
    phone    = serializers.CharField(max_length=11, min_length=11, label="手机号", required=False,
                                     allow_null=True, allow_blank=True, help_text="手机号")

    def create(self, validated_data):
        validated_data["is_active"] = False
        instance = super(UserRegSerializer, self).create(validated_data=validated_data)
        instance.email = "{}{}".format(instance.username, settings.DOMAIN)

        instance.set_password(validated_data["password"])
        instance.id_rsa_key, instance.id_rsa_pub = self.get_sshkey(instance.email)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password =  validated_data.get("password", None)
        if password:
            instance.set_password(password)
            instance.save()
        return instance

    class Meta:
        model = User
        fields = ("username", "password", "name", "id", "phone")