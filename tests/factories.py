import factory.django

from ads.models import Announcement
from category.models import Category
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "wialon"
    email = factory.Faker("email")


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = factory.Faker("name")
    slug = factory.Faker("ean", length=8)


class AnnouncementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Announcement

    name = factory.Faker("name")
    price = 5244
    description = "test text"
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
