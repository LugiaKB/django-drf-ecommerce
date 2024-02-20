from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from ..models import Category
from ..serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

    @extend_schema(request=CategorySerializer, responses=CategorySerializer)
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @extend_schema(
        responses=CategorySerializer,
    )
    def retrieve(self, request, pk=None):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    @extend_schema(request=CategorySerializer, responses=CategorySerializer)
    def update(self, request, pk=None):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @extend_schema(request=CategorySerializer, responses=CategorySerializer)
    def partial_update(self, request, pk=None):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        category = Category.objects.get(id=pk)
        category.delete()
        return Response(status=204)
