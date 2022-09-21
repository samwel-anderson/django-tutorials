from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class Books(models.Model):
    BOOK_STATUS = (
        ('issued', 'Issued'),
        ('not-issued', 'Not Issued'),
    )
    book_id = models.CharField(max_length=10)
    bookname = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    category = models.CharField(max_length=10)
    status = models.CharField('Status', max_length=20, choices=BOOK_STATUS, default='not-issued')
    created_at = models.DateTimeField(verbose_name='Created time', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated time', auto_now=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return str(self.bookname) + "[" + str(self.book_id) + ']'

