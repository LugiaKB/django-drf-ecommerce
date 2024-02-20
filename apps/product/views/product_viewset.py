from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from ..models import Product
from ..serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @extend_schema(request=ProductSerializer, responses=ProductSerializer)
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @extend_schema(
        responses=ProductSerializer,
    )
    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @extend_schema(request=ProductSerializer, responses=ProductSerializer)
    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @extend_schema(request=ProductSerializer, responses=ProductSerializer)
    def partial_update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=204)
