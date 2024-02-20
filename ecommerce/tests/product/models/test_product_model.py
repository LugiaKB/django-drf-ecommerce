import pytest

pytestmark = [pytest.mark.django_db]


class TestProductModel:
    def test_str_method(self, product_factory):
        # arrange
        entity = product_factory()

        # act
        text = entity.__str__()

        # assert
        assert text == entity.name
