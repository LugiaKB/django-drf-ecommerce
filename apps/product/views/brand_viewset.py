from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from ..models import Brand
from ..serializers import BrandSerializer


class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @extend_schema(request=BrandSerializer, responses=BrandSerializer)
    def create(self, request):
        serializer = BrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @extend_schema(
        responses=BrandSerializer,
    )
    def retrieve(self, request, pk=None):
        brand = Brand.objects.get(id=pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

    @extend_schema(request=BrandSerializer, responses=BrandSerializer)
    def update(self, request, pk=None):
        brand = Brand.objects.get(id=pk)
        serializer = BrandSerializer(brand, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @extend_schema(request=BrandSerializer, responses=BrandSerializer)
    def partial_update(self, request, pk=None):
        brand = Brand.objects.get(id=pk)
        serializer = BrandSerializer(brand, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        brand = Brand.objects.get(id=pk)
        brand.delete()
        return Response(status=204)
