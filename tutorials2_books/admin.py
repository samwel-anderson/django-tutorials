from django.contrib import admin

# Register your models here.
from tutorials2_books.forms.issue_book_forms import IssueBookForm
from tutorials2_books.models import Books, IssuedBooks


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'bookname', 'status')
    list_display_links = ('id', 'bookname')
    search_fields = ('id', 'book_id', 'bookname', 'subject', 'status')
    ordering = ['-created_at', '-id']
    list_filter = ['status', 'created_at', 'updated_at']
    list_per_page = 10


@admin.register(IssuedBooks)
class IssuedBooksAdmin(admin.ModelAdmin):
    form = IssueBookForm
    list_display = ('id', 'book', 'issued_date', 'expiry_date')
    list_display_links = ('book', 'issued_date',)
    search_fields = ('id', 'book__id', 'book__book_id', 'book__bookname')
    ordering = ['id']
    list_filter = ['created_at', 'updated_at']
    list_per_page = 20

