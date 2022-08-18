from rest_framework.pagination import PageNumberPagination
# http://127.0.0.1:8000/api/customer/?page=1&page_size=5


class LargePagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 200


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
