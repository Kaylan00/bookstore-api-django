
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import BookViewSet, AuthorViewSet, GenreViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]