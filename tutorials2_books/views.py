from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
# Listing Page
from tutorials2_books.models_base import Books


def index(request):
    books = Books.objects.all()
    # if with filter and order
    # books = Books.objects.filter(status='issued').order_by('-id')

    page = request.GET.get('page', 1)

    paginator = Paginator(books, 2)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        print('page provided not an Integer')
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'books': books})
