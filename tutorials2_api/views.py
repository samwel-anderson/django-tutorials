from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from tutorials2_api.serializers import CustomTokenObtainPairSerializer


class CustomTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer
