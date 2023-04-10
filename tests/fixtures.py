import pytest


@pytest.fixture
@pytest.mark.django_db
def jwt_access_token(client, django_user_model):
    username = "test_user"
    password = "test_password"

    django_user_model.objects.create_user(
        username=username, password=password, role='admin'
    )

    response = client.post(
        "/users/token/",
        {"username": username, "password": password},
    )

    return response.data["access"]


@pytest.fixture
@pytest.mark.django_db
def user_with_jwt_access_token(client, django_user_model):
    username = "test_user"
    password = "test_password"

    user_jwt =  django_user_model.objects.create_user(
        username=username, password=password, role='admin'
    )

    response = client.post(
        "/users/token/",
        {"username": username, "password": password},
    )

    return user_jwt, response.data["access"]
