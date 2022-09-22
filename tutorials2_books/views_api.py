from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
# Listing Page
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from tutorials2_books.models_base import Books
from tutorials2_books.serializers import BooksSerializer


class BooksViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
