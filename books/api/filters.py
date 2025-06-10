import django_filters
from ..models import Book

class BookFilter(django_filters.FilterSet):
   
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Filter by book title (contains)' 
    )
    genre_name = django_filters.CharFilter(
        field_name='genres__name',
        lookup_expr='icontains',
        label='Filter by genre name (contains)'
    )
    published_date = django_filters.DateFromToRangeFilter(
        field_name='published_date',
        label='Publication Date Range (use "published_date_after" and "published_date_before")'
    )

    class Meta:
        model = Book
        fields = ['language']