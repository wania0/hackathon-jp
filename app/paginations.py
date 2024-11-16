from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 1  # Customize page size for this view
    page_size_query_param = "page_size"
    max_page_size = 100