# from django.contrib.auth import views
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

from tutorials2_books.views_api import BooksListCreateAPIView, PollList, BooksListAPIView
from . import views
from .views import CustomTokenPairView

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # DEFAULT TOKEN AUTHENTICATION
    path('auth/', CustomTokenPairView.as_view(), name='token_obtain_pair'),  # CUSTOM TOKEN AUTHENTICATION

    path('listcreate', BooksListCreateAPIView.as_view()),
    path('apiview', PollList.as_view()),
    path('listview', BooksListAPIView.as_view()),


    path('books/', include('tutorials2_books.urls_api')),
]
