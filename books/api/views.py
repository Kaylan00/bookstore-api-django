from rest_framework import viewsets 
from .permissions import IsOwnerOrReadOnly
from ..models import Book, Author, Genre, Review 
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, ReviewSerializer 
from .filters import BookFilter

class BookViewSet(viewsets.ModelViewSet):
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
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)