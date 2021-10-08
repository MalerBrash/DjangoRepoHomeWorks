from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['id', 'title', 'description']
    pagination_class = PageNumberPagination


class StockViewSet(ModelViewSet):

    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ['products']
    search_fields = ['products__title']
    pagination_class = PageNumberPagination
