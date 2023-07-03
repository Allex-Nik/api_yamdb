from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import latin_alphanumeric_validator

User = get_user_model()

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название категории',
        help_text='Выберите категорию произведения'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        validators=[latin_alphanumeric_validator]
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название жанра',
        help_text='Выберите жанр произведения'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        validators=[latin_alphanumeric_validator]
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'

    def __str__(self):
        return self.name


class Title(models.Model):  # Еще есть идея попробовать
    # Добавить поле, которое будет варьироваться
    # в зависимости от выбранной категории произведения: "автор" для книги, "режиссер" для фильма
    # и "исполнитель" для песни. Если время останется
    name = models.CharField(
        max_length=100,
        verbose_name='Название произведения',
        help_text='Укажите название произведения'
    )
    date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата релиза',
        help_text='Выберите дату релиза'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание произведения',
        help_text='Добавьте описание произведения'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='titles'
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='titles'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Произведение'

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='reviews'
    )
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                MaxValueValidator(10)])
    pub_date = models.DateTimeField(
        'Дата публикации', 
        auto_now_add=True
    )
    title = models.ForeignKey(
        Title, 
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    def __str__(self):
        return self.text


    class Meta:
        ordering = ["-pub_date"]
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], 
                name='review_unique'
            )
        ]
        verbose_name = 'Отзыв'


class Comment(models.Model):
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    review = models.ForeignKey(
        Review, 
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', 
        auto_now_add=True, 
        db_index=True
    )

    def __str__(self):
        return self.text


    class Meta:
        ordering = ["id"]
        verbose_name = 'Комментарий'
