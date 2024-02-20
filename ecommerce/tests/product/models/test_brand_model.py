import pytest

pytestmark = [pytest.mark.django_db]


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # arrange
        entity = brand_factory()

        # act
        text = entity.__str__()

        # assert
        assert text == entity.name
