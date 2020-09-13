from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ItemPagination(PageNumberPagination):
    page_size = 50
    def get_paginated_response(self, data):
        return Response(data)