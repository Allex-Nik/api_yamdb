# Generated by Django 3.2 on 2023-07-05 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20230705_1323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.RemoveConstraint(
            model_name='review',
            name='review_unique',
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_title_author'),
        ),
    ]
