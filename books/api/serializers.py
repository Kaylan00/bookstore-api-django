# Em: books/api/serializers.py

from rest_framework import serializers
from ..models import Book, Author, Genre, Review
from .validators import validate_publication_date, validate_isbn

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'comment', 'created_at']

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    
    isbn = serializers.CharField(validators=[validate_isbn])
    published_date = serializers.DateField(validators=[validate_publication_date], required=False)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'authors', 'genres', 'synopsis',
            'cover_image_url', 'page_count', 'language', 'published_date',
            'price', 'stock', 'created_by', 'reviews', 'isbn'
        ]
    def validate_price(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value