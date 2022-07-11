from .models import Inventario, Registro
from rest_framework import serializers, pagination
from ..Informacionapp.serializers import ProductoSerializer, SucursalSerializer, ClienteSerializer


class InventarioSerializer(serializers.Serializer):
    Cliente = ClienteSerializer(source="clienteFK")
    Sucursal = SucursalSerializer(source="sucursalFK")
    Fecha = serializers.DateField(source='fecha')


class RegistroSerializer(serializers.Serializer):
    Inventario =serializers.CharField(source="inventarioFK")
    Producto = serializers.CharField(source="productoFK")
    Inventario_Final = serializers.IntegerField(source="cantidad")


class AllRegistroSerializer(serializers.Serializer):

    Inventario = InventarioSerializer(source="inventarioFK")
    Producto = ProductoSerializer(source="productoFK")
    Inventario_Final = serializers.IntegerField(source="cantidad")


class InventarioPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100
