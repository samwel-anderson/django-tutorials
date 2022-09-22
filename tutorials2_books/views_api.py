from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
# Listing Page
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from tutorials2_books.models_base import Books
from tutorials2_books.serializers import BooksSerializer


class BooksViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BooksSerializer
    queryset = Books.objects.all()


class BooksListCreateAPIView(ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    # permission_classes = [IsAdminUser]


class PollList(APIView):
    object_response = openapi.Response('Response Format', BooksSerializer)

    @swagger_auto_schema(responses={200: object_response})
    def get(self, request):
        polls = Books.objects.all()[:20]
        data = BooksSerializer(polls, many=True).data
        res = {
            "id": '1',
            "name": 'sample name',
            "nick-name": 'rick ross'
        }
        return Response(data, status.HTTP_200_OK)

    def post(self, request, format=None):
        res = {
            "id": '1',
            "name": 'sample name',
            "nick-name": 'rick ross'
        }
        return Response(res, status.HTTP_201_CREATED)

        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
