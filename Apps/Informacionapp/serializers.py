from dataclasses import field
from rest_framework import serializers,pagination
from .models import Cliente, Producto, Sucursal


class ClienteSerializer(serializers.Serializer):
    GLN_Cliente=serializers.IntegerField(source="GLN")


class SucursalSerializer(serializers.Serializer):
    GLN_Sucrusal=serializers.IntegerField(source="GLN")


class ProductoSerializer(serializers.Serializer):
    Gtin_Producto=serializers.IntegerField(source="GLN")
    PrecioUnidad=serializers.DecimalField(source="precio", max_digits=10, decimal_places=2)
class InfoPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100