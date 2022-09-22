from django.db import models

# Create your models here.
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class PaginationOfPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PaginationOfLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 50


class PaginationOfCursorPagination(CursorPagination):
    page_size = 2
    cursor_query_param = 'c'
    ordering = '-id'
