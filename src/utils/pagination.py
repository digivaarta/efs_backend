from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    def get_page(self):
        if self.page.paginator.num_pages is not None:
            return self.page.paginator.num_pages
        return 0

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'has_next': self.get_page(),
            'page_number': self.page.number,
            'page_size': self.page_size,
            'results': data,
        })
