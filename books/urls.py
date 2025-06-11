
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .api.views import BookViewSet, AuthorViewSet, GenreViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'genres', GenreViewSet, basename='genre')

books_router = routers.NestedSimpleRouter(router, r'books', lookup='book')
books_router.register(r'reviews', ReviewViewSet, basename='book-reviews')

urlpatterns = router.urls + books_router.urls