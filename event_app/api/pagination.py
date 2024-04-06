from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    '''
    Пользовательская пагинация для представлений.
    '''
    page_size = 6
