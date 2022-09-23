from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
# Listing Page
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from tutorials2_api.paginations import PaginationOfPageNumberPagination, PaginationOfLimitOffsetPagination, \
    PaginationOfCursorPagination
from tutorials2_api.permissions import CustomDjangoModelPermission, IsStudent
from tutorials2_books.models_base import Books
from tutorials2_books.serializers import BooksSerializer


class BooksViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BooksSerializer
    queryset = Books.objects.all()


class BooksListCreateAPIView(ListCreateAPIView):
    # queryset = Books.objects.all()
    serializer_class = BooksSerializer
    # permission_classes = [IsAdminUser]

    search_param = openapi.Parameter('category', in_=openapi.IN_QUERY,
                                     description='Category Name ',
                                     type=openapi.TYPE_STRING, )

    @swagger_auto_schema(manual_parameters=[search_param])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category is None:
            raise ValidationError('category is required')
            # return Response('category is required', status=status.HTTP_400_BAD_REQUEST)
        queryset = Books.objects.filter(category=category).order_by('id')
        return queryset

    def post(self, request, *args, **kwargs):
        lonee_id = request.data.get('lonee_id')
        if lonee_id is None:
            raise ValidationError('required parameters are missing')
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


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
        return Response(res, status.HTTP_200_OK)

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


class BooksListAPIView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    pagination_class = PaginationOfCursorPagination
    # THE LIST BELOW IS AND
    permission_classes = [IsStudent]
