import pytest

pytestmark = [pytest.mark.django_db]


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # arrange
        entity = category_factory()

        # act
        text = entity.__str__()

        # assert
        assert text == entity.name
