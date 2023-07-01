from django.shortcuts import render
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from api_yamdb.reviews.models import Title, Category, Genre, Review
from .serializers import TitleSerializer, CategorySerializer, GenreSerializer, CommentSerializer, ReviewSerializer


class TitleViewSet(viewsets.ModelViewSet):
    pass


class CategoryViewSet(viewsets.ModelViewSet):
    pass


class GenreViewSet(viewsets.ModelViewSet):
    pass


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    #permission_classes = 
    #pagination_class = 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    #permission_classes = 

    def get_review(self):
        return get_object_or_404(Review, id=self.kwargs.get('review_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_review())

    def get_queryset(self):
        return self.get_review().comments.all()
