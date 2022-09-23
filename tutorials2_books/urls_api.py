# from django.contrib.auth import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views_api import BooksViewSet, BooksListCreateAPIView, PollList, BooksListAPIView

router = DefaultRouter()
router.register('viewsettutorials', BooksViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # path('', include(router.urls)),

    # path('books', include(router.urls)),
]