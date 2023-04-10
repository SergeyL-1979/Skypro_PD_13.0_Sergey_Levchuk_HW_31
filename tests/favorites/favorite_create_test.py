import pytest
from rest_framework import status

from tests.factories import AnnouncementFactory


@pytest.mark.django_db
def test_favorite_create(client, user_with_jwt_access_token):
    user, jwt_access_token = user_with_jwt_access_token
    ads_list = AnnouncementFactory.create_batch(10)

    data = {
        "name": "test",
        "ads": [ads.pk for ads in ads_list]
    }

    expected_data = {
        "id": 1,
        "author": user.username,
        "name": "test",
        "ads": [ads.pk for ads in ads_list]
    }

    response = client.post(
        "/selection/",
        data=data,
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {jwt_access_token}"
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data != expected_data
