# Generated by Django 4.1.7 on 2023-04-10 19:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Announcement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=150,
                        validators=[django.core.validators.MinLengthValidator(10)],
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Цена",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "image",
                    models.ImageField(
                        null=True, upload_to="images", verbose_name="Добавить фото"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False, null=True, verbose_name="is_published"
                    ),
                ),
            ],
            options={
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
                "ordering": ["author__username"],
            },
        ),
        migrations.CreateModel(
            name="Favorite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=15)),
                ("ads", models.ManyToManyField(blank=True, to="ads.announcement")),
            ],
            options={
                "verbose_name": "Избранное",
                "verbose_name_plural": "Избранные",
            },
        ),
    ]
