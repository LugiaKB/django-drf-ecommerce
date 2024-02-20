import pytest
import json
from rest_framework import status

pytestmark = [pytest.mark.django_db]


class TestCategoryEndpoint:
    endpoint = "/api/category/"

    def test_category_get(self, category_factory, api_client):
        # arrange
        length = 4
        category_factory.create_batch(length)

        # act
        response = api_client().get(self.endpoint)
        json_response = json.loads(response.content)

        # assert
        assert response.status_code == status.HTTP_200_OK
        assert len(json_response) == length
