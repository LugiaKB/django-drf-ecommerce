from rest_framework import serializers

from ..models import Product
from .brand_serializer import BrandSerializer
from .category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"
