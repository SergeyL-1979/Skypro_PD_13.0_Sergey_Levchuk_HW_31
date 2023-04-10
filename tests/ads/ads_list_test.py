import pytest
from rest_framework import status

from ads.serializers import AnnouncementListSerializer
from tests.factories import AnnouncementFactory


@pytest.mark.django_db
def test_ads_list(client):
    ads_list = AnnouncementFactory.create_batch(10)
    response = client.get("/ad/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data != {
        'count': 10,
        'next': None,
        'previous': None,
        'results': AnnouncementListSerializer(ads_list, many=True).data
    }
