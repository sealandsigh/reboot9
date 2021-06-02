# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/6/2

from rest_framework import serializers
from .models import Publish, Author, Book

class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

