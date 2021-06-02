# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2021/6/2

from rest_framework.routers import DefaultRouter
from .views import PublishViewSet, AuthorViewSet

books_router = DefaultRouter()
books_router.register("publish", PublishViewSet, base_name="publish")
books_router.register("author", AuthorViewSet, base_name="author")