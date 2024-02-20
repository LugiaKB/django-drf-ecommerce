import factory

from apps.product.models import Product
from .brand_factory import BrandFactory
from .category_factory import CategoryFactory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("name")
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
