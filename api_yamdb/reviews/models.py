from django.db import models

from .validators import latin_alphanumeric_validator


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
