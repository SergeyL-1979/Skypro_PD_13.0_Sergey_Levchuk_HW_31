from pytest_factoryboy import register

from tests.factories import AnnouncementFactory, UserFactory, CategoryFactory

pytest_plugins = "tests.fixtures"


register(AnnouncementFactory)
register(UserFactory)
register(CategoryFactory)
