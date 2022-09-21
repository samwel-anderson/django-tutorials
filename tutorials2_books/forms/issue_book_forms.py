from datetime import datetime

from django import forms
from django.db.models import Sum
from django.utils.translation import gettext as _

from tutorials2_books.models import IssuedBooks
from tutorials2_books.models_base import Books


class IssueBookForm(forms.ModelForm):
    def clean(self):
        if self.instance.pk is None:  # add
            book = self.cleaned_data['book']
            book_object = Books.objects.filter(pk=book.pk).first()
            book_issued = IssuedBooks.objects.filter(book=book_object, expiry_date__gte=datetime.today()).order_by(
                '-id').exists()
            if book_issued or book.status == 'issued':
                raise forms.ValidationError({'book': _(f'Book already issued !!!.')})
