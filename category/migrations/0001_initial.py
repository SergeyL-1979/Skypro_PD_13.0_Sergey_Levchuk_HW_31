# Generated by Django 4.1.7 on 2023-04-10 19:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                        max_length=64, unique=True, verbose_name="Наименование"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=10,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(5)],
                        verbose_name="Slug",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
    ]
