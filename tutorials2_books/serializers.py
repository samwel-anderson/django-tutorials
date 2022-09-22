from rest_framework import serializers

from tutorials2_books.models_base import Books


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = (
            'id',
            'book_id',
            'bookname',
            'created_at'
        )
