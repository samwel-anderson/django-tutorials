from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Create your views here.
def index(request):
    return HttpResponse("Home Page")

