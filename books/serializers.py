from rest_framework import serializers
from books.models import Book, LANGUAGE_CHOICES, STYLE_CHOICES


class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Book
        fields = ['created', 'title', 'authors', 'publisher', 'publication_date', 'number_of_pages', 'author']


from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'books']