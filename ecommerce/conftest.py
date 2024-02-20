from pytest_factoryboy import register
from .tests.factories.product import BrandFactory, CategoryFactory, ProductFactory


register(BrandFactory)
register(CategoryFactory)
register(ProductFactory)
