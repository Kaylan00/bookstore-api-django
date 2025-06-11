from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly
from ..models import Book, Author, Genre, Review
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, ReviewSerializer
from .filters import BookFilter

class BookViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que os livros sejam vistos ou editados.
    """
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filterset_class = BookFilter

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para reviews, aninhado sob os livros.
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk'])

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs['book_pk'])
        serializer.save(user=self.request.user, book=book)