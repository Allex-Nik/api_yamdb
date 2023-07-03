from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from reviews.models import Comment, Review


class TitleSerializer(serializers.ModelSerializer):
    pass


class CategorySerializer(serializers.ModelSerializer):
    pass


class GenreSerializer(serializers.ModelSerializer):
    pass


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username', 
        read_only=True
    )

    class Meta:
        model = Review
        fields = ('id', 'author', 'text', 'rating', 'pub_date')   


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username', 
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'pub_date')
