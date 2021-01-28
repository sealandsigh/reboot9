# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/9/2

from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    def get_page_size(self, request):
        try:
            page_size = int(request.query_params.get("page_size", -1))
            if page_size >= 0:
                return page_size
        except:
            pass
        return self.page_size