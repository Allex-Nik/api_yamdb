# Generated by Django 3.2 on 2023-07-02 14:19

import django.core.validators
from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20230701_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Выберите категорию произведения', max_length=256, unique=True, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, validators=[django.core.validators.RegexValidator('^[-a-zA-Z0-9_]+$', 'Символы латинского алфавита, дефис, цифры и знак подчёркивания')]),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Выберите жанр произведения', max_length=256, unique=True, verbose_name='Название жанра'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True, validators=[django.core.validators.RegexValidator('^[-a-zA-Z0-9_]+$', 'Символы латинского алфавита, дефис, цифры и знак подчёркивания')]),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(help_text='Укажите название произведения', max_length=256, verbose_name='Название произведения'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(blank=True, help_text='Выберите год выпуска', null=True, validators=[reviews.validators.year_validator], verbose_name='Год выпуска'),
        ),
    ]
