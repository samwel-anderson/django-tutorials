# from django.contrib.auth import views
from django.urls import path, include

from . import views

urlpatterns = [
    path('books/', include('tutorials2_books.urls_api')),
]
