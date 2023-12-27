from rest_framework.pagination import PageNumberPagination

class SimplePaginationClass(PageNumberPagination):
    """Conditioned to display the products' data on the web page"""
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 50