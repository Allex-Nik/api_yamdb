from django_filters.rest_framework import CharFilter, NumberFilter, FilterSet

from reviews.models import Title


class TitleFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    category = CharFilter(field_name='category__slug')
    genre = CharFilter(field_name='genre__slug')
    year = NumberFilter()

    class Meta:
        model = Title
        fields = ['name', 'category', 'genre', 'year']
