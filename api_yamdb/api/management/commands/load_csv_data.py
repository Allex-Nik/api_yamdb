from csv import DictReader

from django.core.management.base import BaseCommand

from reviews.models import Category, Genre, Title, GenreToTitle  # Comment, Review
# from api_yamdb.users.models import User


class Command(BaseCommand):
    help = 'Переносит данные из csv файлов в базу данных'

    def handle_category(self):
        for row in DictReader(open('static/data/category.csv')):
            Category.objects.get_or_create(
                id=row[0],
                name=row[1],
                slug=row[2]
            )

    # def handle_comments(self):
    #     for row in DictReader(open('static/data/comments.csv')):
    #         Comment.objects.get_or_create(
    #             id=row[0],
    #             author=row[1],
    #             review=row[2],
    #             text=row[3],
    #             created=row[4]
    #         )

    def handle_genre(self):
        for row in DictReader(open('static/data/genre.csv')):
            Genre.objects.get_or_create(
                id=row[0],
                name=row[1],
                slug=row[2]
            )

    # def handle_review(self):
    #     for row in DictReader(open('static/data/review.csv')):
    #         Review.objects.get_or_create(
    #             id=row[0],
    #             name=row[1],
    #             slug=row[2]
    #         )

    def handle_titles(self):
        for row in DictReader(open('static/data/titles.csv')):
            Title.objects.get_or_create(
                id=row[0],
                name=row[1],
                year=row[2],
                category_id=row[3]
            )

    # def handle_users(self):
    #     for row in DictReader(open('static/data/users.csv')):
    #         User.objects.get_or_create(
    #             id=row[0],
    #             username=row[1],
    #             email=row[2],
    #             role=row[3],
    #             bio=row[4],
    #             first_name=row[5],
    #             last_name=row[6]
    #         )

    def handle_genre_title(self):
        for row in DictReader(open('static/data/genre_title.csv')):
            GenreToTitle.objects.get_or_create(
                id=row[0],
                title=row[1],
                genre=row[2],
            )

    def handle(self, *args, **options):
        self.handle_category()
        self.handle_comments()
        self.handle_genre()
        self.handle_review()
        self.handle_titles()
        self.handle_users()
        self.handle_genre_title()
