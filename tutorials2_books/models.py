from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
from tutorials2_books.models_base import Books


def expiry():
    return datetime.today() + timedelta(days=15)


class IssuedBooks(models.Model):
    book = models.ForeignKey(Books, null=True, blank=True, on_delete=models.RESTRICT)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
    created_at = models.DateTimeField(verbose_name='Created time', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated time', auto_now=True)

    class Meta:
        verbose_name = "Issued Book"
        verbose_name_plural = "Issued Books"

    def __str__(self):
        return f'{str(self.book.bookname)}'

    def save(self, *args, **kwargs):
        if not self.pk:  # IF NO PK Then it is when adding
            store = self.book
            print(f'store book : {store}')

            book_issued = IssuedBooks.objects.filter(book=self.book, expiry_date__gte=datetime.today()).order_by(
                '-id').exists()
            if book_issued or self.book.status == 'issued':
                raise ValidationError({'book': _(f'Book already issued !!!.')})
            else:
                store.status = "issued"
                store.save()
                super().save(*args, **kwargs)
        else:
            store = self.book
            if self.book.status == 'issued':
                store.status = "issued"
                store.save()
        return super().save(*args, **kwargs)
