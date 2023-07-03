from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from api_yamdb.reviews.models import Title, Category, Genre
from .filters import TitleFilter
from .serializers import TitleSerializer, CategorySerializer, GenreSerializer

#  Нужно добавить права доступа для вьюсетов


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
