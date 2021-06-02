# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/6/2

from rest_framework import serializers
from .models import Publish, Author, Book

class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"

    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        self.Meta.model.objects.filter(id=instance.id).update(**validated_data)
        return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"



