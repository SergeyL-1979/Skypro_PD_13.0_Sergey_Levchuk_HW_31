import pytest
from rest_framework import status


@pytest.mark.django_db
def test_ads_create(client, category, jwt_access_token):

    data = {
        "author": "test_user",
        "name": "test text yrrwdsf",
        "price": 65,
        "category": category.name
    }

    expected_data = {
        "id": 1,
        "author": "test_user",
        "category": category.name,
        "name": "test text yrrwdsf",
        "price": 65,
        "description": None,
        "image": None,
        "is_published": False
    }

    response = client.post(
        "/ad/create/",
        data=data,
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {jwt_access_token}"
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == expected_data
