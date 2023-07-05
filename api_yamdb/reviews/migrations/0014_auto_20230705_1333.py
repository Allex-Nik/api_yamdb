# Generated by Django 3.2 on 2023-07-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_auto_20230705_1330'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='review_unique',
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_author_review'),
        ),
    ]
