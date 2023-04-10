import pytest
from rest_framework import status

from ads.serializers import AnnouncementDetailSerializer
from tests.factories import AnnouncementFactory


@pytest.mark.django_db
def test_ads_retrieve(client, jwt_access_token):
    ads = AnnouncementFactory.create()

    response = client.get(f"/ad/{ads.pk}/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = client.get(f"/ad/{ads.pk}/", HTTP_AUTHORIZATION=f"Bearer {jwt_access_token}")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == AnnouncementDetailSerializer(ads).data
