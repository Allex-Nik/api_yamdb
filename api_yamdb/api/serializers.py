from rest_framework import serializers
from api_yamdb.reviews.models import Title, Category, Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'slug']


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer
    genre = GenreSerializer(many=True)

    class Meta:
        model = Title
        fields = ['id', 'name', 'year', 'description', 'category', 'genre']
