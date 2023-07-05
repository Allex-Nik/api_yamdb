from django.core.validators import RegexValidator
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Comment, Review, Title, Category, Genre
from users.models import User


class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=[RegexValidator(regex=r'^[\w.@+-]+$')]
    )
    email = serializers.EmailField(
        max_length=254,
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Нельзя создать пользователя с таким именем')
        return value


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')

    def validate(self, data):
        username = data['username']
        user = get_object_or_404(User, username=username)
        if user.confirmation_code != data['confirmation_code']:
            raise serializers.ValidationError('Неверный код подтверждения')
        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )

        
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
        

class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username', 
        read_only=True,
    )

    class Meta:
        model = Review
        fields = ('id', 'author', 'text', 'score', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username', 
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'pub_date')


class TitleSerializerRead(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    score = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'description', 'year', 'category', 'genre', 'score'
        )
        read_only_fields = ('id',)

    def get_score(self, obj):
        obj = obj.reviews.all().aggregate(score=Avg('score'))
        return obj['score']


class TitleSerializerCreate(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'description', 'year', 'category', 'genre')
